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
