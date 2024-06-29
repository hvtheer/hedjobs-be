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
from .email import EmailService
from app.utils import *
from app.repositories import *
from app.config.constants import *
from app.config.settings import get_settings

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

        self.m_education_repository = MEducationRepository(session)
        self.m_position_repository = MPositionRepository(session)
        self.m_stage_repository = MStageRepository(session)

        self.rate_career_matching_repository = RateCareerMatchingRepository(session)
        self.rate_skill_matching_repository = RateSkillMatchingRepository(session)
        self.rate_city_matching_repository = RateCityMatchingRepository(session)
        self.rate_certificate_matching_repository = RateCertificateMatchingRepository(
            session
        )

        self.application_repository = ApplicationRepository(session)

    def _create_student(self, user):
        self.create_user_role_entity(user, UserRole.STUDENT, self.student_repository)

    def _create_recruiter(self, user):
        self.create_user_role_entity(
            user, UserRole.RECRUITER, self.recruiter_repository
        )

    def create_user_role_entity(self, user, role, repository):
        if user.role == role:
            new_entity = {
                f"{role.lower()}_id": user.user_id,
                "name": user.name,
                "email": user.email,
                "phone_number": user.phone_number,
            }
            repository.create(new_entity)

    def _get_record_or_404(
        self,
        repository,
        condition,
        error_message=ErrorMessage.NOT_FOUND,
        status_code=status.HTTP_404_NOT_FOUND,
    ):
        record = repository.get_first_by_condition(condition)
        if not record:
            raise CustomException(status_code=status_code, detail=error_message)
        return record

    def _ensure_unique_record(
        self,
        repository,
        condition,
        error_message=ErrorMessage.ALREADY_EXISTS,
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    ):
        if repository.get_first_by_condition(condition):
            raise CustomException(status_code=status_code, detail=error_message)

    def _create_related_entities(
        self, entity_id, entity_id_attr, related_data_to_create, related_repository
    ):
        entities = []
        for data in related_data_to_create:
            data[entity_id_attr] = entity_id
            related_entity = related_repository.create(data)
            entities.append(related_entity)
        return entities

    def _delete_related_entities(
        self, related_data_to_delete, related_repository, related_model, related_id_attr
    ):
        for data in related_data_to_delete:
            condition = getattr(related_model, related_id_attr) == getattr(
                data, related_id_attr
            )
            related_repository.delete_by_condition(condition)

    def _update_related_entities(
        self,
        entity_id,
        entity_id_attr,
        related_data,
        related_repository,
        related_model,
        related_id_attr,
    ):
        # Get existing related data by entity id attribute like job_id
        existing_related_data = related_repository.get_all(
            condition=getattr(related_model, entity_id_attr) == entity_id
        )
        self._delete_related_entities(
            existing_related_data, related_repository, related_model, related_id_attr
        )
        created_data = self._create_related_entities(
            entity_id, entity_id_attr, related_data, related_repository
        )

        return created_data
