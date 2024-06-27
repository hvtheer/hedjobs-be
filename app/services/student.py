from fastapi import status
from sqlalchemy.orm import Session

from app.services.base import BaseService
from app.responses.base import Page, SuccessResponse
from app.responses.student import StudentDetailsResponse
from app.models import *
from app.config.constants import ErrorMessage, SuccessMessage, UserRole
from app.utils.exception import CustomException
from app.utils import *


class StudentService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session)

    async def get_student_by_id(self, student_id):
        student = get_record_or_404(
            repository=self.student_repository,
            condition=Student.student_id == student_id,
        )
        skills = self.student_skill_repository.get_all(
            condition=StudentSkill.student_id == student_id
        )
        certificates = self.student_certificate_repository.get_all(
            condition=StudentCertificate.student_id == student_id
        )
        educations = self.student_education_repository.get_all(
            condition=StudentEducation.student_id == student_id
        )
        careers = self.student_career_repository.get_all(
            condition=StudentCareer.student_id == student_id
        )
        data = StudentDetailsResponse(
            student=student,
            skills=skills,
            certificates=certificates,
            educations=educations,
            careers=careers,
        )
        return SuccessResponse(message=SuccessMessage.SUCCESS, data=data)

    async def update_student_details(
        self,
        user_id,
        student_id,
        student_data,
        skills_data,
        certificates_data,
        educations_data,
        careers_data,
    ):
        if user_id != student_id:
            raise CustomException(
                status_code=status.HTTP_403_FORBIDDEN,
                message=ErrorMessage.FORBIDDEN,
            )
        student = get_record_or_404(
            repository=self.student_repository,
            condition=Student.student_id == student_id,
        )
        student_data["student_id"] = student_id
        student = self.student_repository.update_by_id(student_id, student_data)
        skills = update_related_entities(
            student_id,
            "student_id",
            skills_data,
            self.student_skill_repository,
            StudentSkill,
            "skill_id",
        )
        certificates = update_related_entities(
            student_id,
            "student_id",
            certificates_data,
            self.student_certificate_repository,
            StudentCertificate,
            "certificate_id",
        )
        educations = update_related_entities(
            student_id,
            "student_id",
            educations_data,
            self.student_education_repository,
            StudentEducation,
            "education_id",
        )
        careers = update_related_entities(
            student_id,
            "student_id",
            careers_data,
            self.student_career_repository,
            StudentCareer,
            "career_id",
        )
        # return {
        #     "student": student,
        #     "skills": skills,
        #     "certificates": certificates,
        #     "educations": educations,
        #     "careers": careers,
        # }
        return StudentDetailsResponse(
            student=student,
            skills=skills,
            certificates=certificates,
            educations=educations,
            careers=careers,
        )
        # return SuccessResponse(message=SuccessMessage.UPDATED, data=student)
