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
from app.models import *
from app.models.recruiter import Recruiter
from app.repositories.company import CompanyRepository
from .email import EmailService
from app.utils.string import unique_string
from app.utils.email_context import USER_VERIFY_ACCOUNT
from app.utils.exception import CustomException
from app.utils import *
from app.repositories import *
from app.config.constants import ErrorMessage, UserRole, SuccessMessage
from app.config.settings import get_settings
from app.responses.base import SuccessResponse, InfoResponse

settings = get_settings()


class BaseService:
    def __init__(self, session: Session):
        self.session = session
        self.email_service = EmailService()
        self.user_repository = UserRepository(session)
        self.user_token_repository = UserTokenRepository(session)

        self.student_repository = StudentRepository(session)
        self.student_skill_repository = StudentSkillRepository(session)
        self.student_education_repository = StudentEducationRepository(session)
        self.student_certificate_repository = StudentCertificateRepository(session)
        self.student_career_repository = StudentCareerRepository(session)

        self.recruiter_repository = RecruiterRepository(session)
        self.company_repository = CompanyRepository(session)
        self.job_repository = JobRepository(session)
        self.job_skill_repository = JobSkillRepository(session)
        self.job_education_repository = JobEducationRepository(session)
        self.job_certificate_repository = JobCertificateRepository(session)

        self.m_career_repository = MCareerRepository(session)
        self.m_position_repository = MPositionRepository(session)
        self.m_skill_repository = MSkillRepository(session)
        self.m_city_repository = MCityRepository(session)

    def _create_student(self, user):
        self.create_user_role_entity(user, UserRole.STUDENT, self.student_repository)

    def _create_recruiter(self, user):
        self.create_user_role_entity(
            user, UserRole.RECRUITER, self.recruiter_repository
        )

    def calculate_matching_score(
        student,
        job,
    ):
        pass
