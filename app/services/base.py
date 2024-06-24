from datetime import datetime, timedelta
import logging
from sqlalchemy.orm import Session
from fastapi import status
from typing import Dict, Any

from app.config.security import (
    generate_token,
    get_token_payload,
    str_encode,
    verify_password,
    hash_password,
)
from app.models import User, Student, UserToken
from app.models.recruiter import Recruiter
from app.repositories.company import CompanyRepository
from .email import EmailService
from app.utils.string import unique_string
from app.utils.email_context import USER_VERIFY_ACCOUNT
from app.utils.exception import CustomException
from app.repositories import (
    UserRepository,
    StudentRepository,
    UserTokenRepository,
    RecruiterRepository,
    CompanyRepository,
    JobRepository,
    JobSkillRepository,
    JobEducationRepository,
    JobCertificateRepository,
)
from app.config.constants import ErrorMessage, UserRole, SuccessMessage
from app.config.settings import get_settings
from app.responses.base import SuccessResponse, InfoResponse

settings = get_settings()


class BaseService:
    def __init__(self, session: Session):
        self.session = session
        self.user_repository = UserRepository(session)
        self.student_repository = StudentRepository(session)
        self.user_token_repository = UserTokenRepository(session)
        self.recruiter_repository = RecruiterRepository(session)
        self.company_repository = CompanyRepository(session)
        self.email_service = EmailService()
        self.job_repository = JobRepository(session)
        self.job_skill_repository = JobSkillRepository(session)
        self.job_education_repository = JobEducationRepository(session)
        self.job_certificate_repository = JobCertificateRepository(session)

    def _create_student(self, user):
        if user.role == UserRole.STUDENT:
            new_student = {
                "student_id": user.user_id,
                "name": user.name,
                "email": user.email,
                "phone_number": user.phone_number,
            }
            self.student_repository.create(new_student)

    def _create_recruiter(self, user):
        if user.role == UserRole.RECRUITER:
            new_recruiter = {
                "recruiter_id": user.user_id,
                "name": user.name,
                "email": user.email,
                "phone_number": user.phone_number,
            }
            self.recruiter_repository.create(new_recruiter)

    def _get_user_by_email(self, email):
        user = self.user_repository.get_user_by_email(email)
        if not user:
            return None
        return user
