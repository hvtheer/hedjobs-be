from datetime import datetime, timedelta
import logging
from sqlalchemy.orm import Session
from fastapi import status
from typing import Dict, Any

import app.config.security
from app.models import User, Student
from app.services import EmailService
from app.utils.string import unique_string
from app.utils.email_context import USER_VERIFY_ACCOUNT
from app.utils.exception import CustomException
from app.repositories import UserRepository, StudentRepository, UserTokenRepository
from app.config.constants import ErrorMessage, UserRole
from app.config.settings import get_settings
from app.services.base import BaseService

settings = get_settings()

class UserService(BaseService):

    def __init__(self, session: Session):
        self.user_repository = UserRepository(session)
        self.student_repository = StudentRepository(session)
    
    async def get_all_users(self):
        return self.user_repository.get_all(order_by=User.name)
    
    # async def get_me(self, user_id: int):
    #     user = self.user_repository.get_by_id(user_id)
    #     if not user:
    #         raise CustomException(status_code=status.HTTP_404_NOT_FOUND, detail=ErrorMessage.NOT_FOUND)
    #     return user

    # async def create_user(self, new_user):
    #     try:
    #         if self.user_repository.get_user_by_email(new_user['email']):
    #             raise CustomException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=ErrorMessage.ALREADY_EXISTS)
    #         user = self.user_repository.create(new_user)
    #         self._create_student_if_needed(user)
    #         return user
    #     except CustomException as e:
    #         raise e
    #     except Exception as e:
    #         logging.exception(f"An error occurred in create_user for model: {e}")
    #         raise CustomException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

