from datetime import datetime, timedelta
import logging
from sqlalchemy.orm import Session
from fastapi import status
from typing import Dict, Any

from app.config.security import generate_token, get_token_payload, str_encode, verify_password, hash_password
from app.models import User, Student
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
        self.user_repository = UserRepository(session)
        self.student_repository = StudentRepository(session)
        self.user_token_repository = UserTokenRepository(session)

    def create_user(self, new_user):
        if self.user_repository.get_all_by_column(User.email, new_user['email']):
            raise CustomException(status_code=status.HTTP_400_BAD_REQUEST, detail=ErrorMessage.ALREADY_EXISTS)
        new_user['password'] =  hash_password(new_user['password'])
        user_instance = User(**new_user)
        return self.user_repository.create(user_instance)

    async def register(self, new_user, background):
        user = self.create_user(new_user)

        if user.role == UserRole.STUDENT:
            new_student = {
                'student_id': user.user_id,
                'name': user.name,
                'email': user.email,
                'phone_number': user.phone_number
            }
            student_instance = Student(**new_student)
            self.student_repository.create(student_instance)

        await EmailService.send_account_verification_email(user, background_tasks=background)
        return SuccessResponse(message=SuccessMessage.CREATED, data=user)

    async def activate_user_account(self, data, background_tasks):
        users = self.user_repository.get_all_by_column(User.email, data.email)
        if not users:
            raise CustomException(status_code=status.HTTP_400_BAD_REQUEST, detail="This link is not valid.")

        user = users[0]
        user_token = user.get_context_string(context=USER_VERIFY_ACCOUNT)
        print("user_token", user_token)
        print("data_token", data.token)
        try:
            token_valid = verify_password(user_token, data.token)
            print("token_valid", token_valid)
        except Exception as verify_exec:
            logging.exception(verify_exec)
            token_valid = False
        if not token_valid:
            raise CustomException(status_code=status.HTTP_400_BAD_REQUEST, detail="This link either expired or not valid.")
        
        updated_user = {
            'is_active': True,
            'verified_at': datetime.utcnow()
        }
        self.user_repository.update_by_condition({'email': user.email}, updated_user)
        # Activation confirmation email
        await EmailService.send_account_activation_confirmation_email(user, background_tasks)
        return user

    async def get_login_token(self, data):
        users = self.user_repository.get_all_by_column(User.email, data.username)
        user = users[0]
        if not user or not verify_password(data.password, user.password):
            raise CustomException(status_code=status.HTTP_400_BAD_REQUEST, detail=ErrorMessage.INCORRECT)

        if not user.verified_at or not user.is_active:
            raise CustomException(status_code=status.HTTP_400_BAD_REQUEST, detail=ErrorMessage.INACTIVE_ACCOUNT)
        
        updated_user = {
            'last_login_at': datetime.utcnow()
        }
        self.user_repository.update_by_id(user.user_id, updated_user)
        return self._generate_tokens(user)

    def _generate_tokens(self, user):
        refresh_key = unique_string(100)
        access_key = unique_string(50)
        rt_expires = timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)

        user_token = {
            'user_id': user.user_id,
            'refresh_key': refresh_key,
            'access_key': access_key,
            'expires_at': datetime.utcnow() + rt_expires
        }
        user_token = self.user_token_repository.create(user_token)

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
