from datetime import datetime, timedelta
import logging
from sqlalchemy.orm import Session
from fastapi import status
from typing import Dict, Any

from app.config.security import generate_token, get_token_payload, str_encode, verify_password, hash_password
from app.models import User, Student, UserToken
from .email import EmailService
from app.utils.string import unique_string
from app.utils.email_context import USER_VERIFY_ACCOUNT
from app.utils.exception import CustomException
from app.repositories import UserRepository, StudentRepository, UserTokenRepository
from app.config.constants import ErrorMessage, UserRole, SuccessMessage
from app.config.settings import get_settings
from app.responses.base import SuccessResponse

settings = get_settings()

class AuthService:

    def __init__(self, session: Session):
        self.session = session
        self.user_repository = UserRepository(session)
        self.student_repository = StudentRepository(session)
        self.user_token_repository = UserTokenRepository(session)

    async def register(self, new_user, background):
        try:
            user = self.user_repository.create_user(new_user)
            self._create_student_if_needed(user)
            await EmailService.send_account_verification_email(user, background_tasks=background)
            return SuccessResponse(message=SuccessMessage.CREATED, data=user)
        except CustomException as e:
            self.session.rollback()
            raise e
        except Exception as e:
            self.session.rollback()
            logging.exception(f"An error occurred in register for model: {e}")
            raise CustomException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    async def activate_user_account(self, data, background_tasks):
        try:
            user = self._get_user_by_email(data['email'])
            self._validate_token(user, data['token'], USER_VERIFY_ACCOUNT)
            self._update_user_status(user, is_active=True, verified_at=datetime.utcnow())
            await EmailService.send_account_activation_confirmation_email(user, background_tasks)
            return SuccessResponse(message=SuccessMessage.VERIFIED)
        except CustomException as e:
            self.session.rollback()
            raise e
        except Exception as e:
            self.session.rollback()
            logging.exception(e)
            raise CustomException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    async def get_login_token(self, data):
        try:
            user = self._get_user_by_email(data.username)
            self._validate_credentials(user, data.password)
            self._validate_user_status(user)
            self._update_user_status(user, last_login_at=datetime.utcnow())
            data = self._generate_tokens(user)
            return data
        except CustomException as e:
            self.session.rollback()
            raise e
        except Exception as e:
            self.session.rollback()
            logging.exception(e)
            raise CustomException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def _generate_tokens(self, user):
        refresh_key = unique_string(100)
        access_key = unique_string(50)
        rt_expires = timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)

        new_user_token = {
            'user_id': user.user_id,
            'refresh_key': refresh_key,
            'access_key': access_key,
            'expires_at': datetime.utcnow() + rt_expires
        }
        user_token = self.user_token_repository.create(new_user_token)

        at_payload = {
            "sub": str_encode(str(user.user_id)),
            'a': access_key,
            'r': str_encode(str(user_token.user_token_id)),
            'n': str_encode(f"{user.name}")
        }

        at_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = generate_token(at_payload, settings.JWT_SECRET, settings.JWT_ALGORITHM, at_expires)

        rt_payload = {"sub": str_encode(str(user.user_id)), "t": refresh_key, 'a': access_key}
        refresh_token = generate_token(rt_payload, settings.SECRET_KEY, settings.JWT_ALGORITHM, rt_expires)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "expires_in": at_expires.seconds
        }

    def _create_student_if_needed(self, user):
        if user.role == UserRole.STUDENT:
            new_student = {
                'student_id': user.user_id,
                'name': user.name,
                'email': user.email,
                'phone_number': user.phone_number
            }
            self.student_repository.create(new_student)

    def _get_user_by_email(self, email):
        users = self.user_repository.get_all(condition={'email': email})
        if not users:
            raise CustomException(status_code=status.HTTP_400_BAD_REQUEST, detail="This link is not valid.")
        return users[0]

    def _validate_token(self, user, token, context):
        user_token = user.get_context_string(context=context)
        try:
            token_valid = verify_password(user_token, token)
        except Exception as verify_exec:
            logging.exception(verify_exec)
            token_valid = False
        if not token_valid:
            raise CustomException(status_code=status.HTTP_403_FORBIDDEN, detail=ErrorMessage.FORBIDDEN)

    def _validate_credentials(self, user, password):
        if not user or not verify_password(password, user.password):
            raise CustomException(status_code=status.HTTP_400_BAD_REQUEST, detail=ErrorMessage.INCORRECT)

    def _validate_user_status(self, user):
        if not user.verified_at or not user.is_active:
            raise CustomException(status_code=status.HTTP_400_BAD_REQUEST, detail=ErrorMessage.INACTIVE_ACCOUNT)

    def _update_user_status(self, user, **kwargs):
        self.user_repository.update_by_id(user.user_id, kwargs)