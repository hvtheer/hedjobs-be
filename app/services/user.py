from datetime import datetime, timedelta
import logging
from sqlalchemy.orm import Session
from fastapi import status
from typing import Dict, Any

from app.config.security import generate_token, get_token_payload, str_encode, verify_password
from app.models import User, Student
from app.services import EmailService
from app.utils.string import unique_string
from app.utils.email_context import USER_VERIFY_ACCOUNT
from app.utils.exception import CustomException
from app.repositories import UserRepository, StudentRepository, UserTokenRepository
from app.config.constants import ErrorMessage, UserRole
from app.config.settings import get_settings

settings = get_settings()

class UserService:

    def __init__(self, session: Session):
        self.user_repository = UserRepository(session)
        self.student_repository = StudentRepository(session)

    async def get_me(self, user_id: int):
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise CustomException(status_code=status.HTTP_404_NOT_FOUND, detail=ErrorMessage.NOT_FOUND)
        return user

