from fastapi import status
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.models import *
from app.services import *
from app.responses import *
from app.config.constants import *
from app.utils import *


class JobService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session)

    async def create_job_details(
        self,
        staff_id,
        job_data,
        skills_data=None,
        certificates_data=None,
        educations_data=None,
    ):
        company = self._get_record_or_404(
            repository=self.company_repository, condition=Company.staff_id == staff_id
        )
        job_data["company_id"] = company.company_id
        job = self.job_repository.create(job_data)
        skills = self._create_related_entities(
            job.job_id, "job_id", skills_data, self.job_skill_repository
        )
        certificates = self._create_related_entities(
            job.job_id,
            "job_id",
            certificates_data,
            self.job_certificate_repository,
        )
        educations = self._create_related_entities(
            job.job_id, "job_id", educations_data, self.job_education_repository
        )

        job_details = JobDetailsResponse(
            job=job,
            skills=skills,
            certificates=certificates,
            educations=educations,
        )

        return SuccessResponse(message=SuccessMessage.CREATED, data=job_details)

    async def get_job_by_id(self, job_id):
        job = self._get_record_or_404(
            repository=self.job_repository, condition=Job.job_id == job_id
        )
        skills = self.job_skill_repository.get_all(condition=JobSkill.job_id == job_id)
        certificates = self.job_certificate_repository.get_all(
            condition=JobCertificate.job_id == job_id
        )
        educations = self.job_education_repository.get_all(
            condition=JobEducation.job_id == job_id
        )

        job_details = JobDetailsResponse(
            job=job,
            skills=skills,
            certificates=certificates,
            educations=educations,
        )

        return SuccessResponse(message=SuccessMessage.SUCCESS, data=job_details)

    async def get_jobs(
        self,
        keyword,
        skills,
        company_id,
        city_id,
        working_arrangement,
        career_id,
        position_id,
        page,
        size,
        current_user,
    ):
        condition = self._build_job_search_condition(
            keyword,
            skills,
            company_id,
            city_id,
            working_arrangement,
            career_id,
            position_id,
        )
        order_by = None
        pagination = {"page": page, "size": size}

        # If the user is a recruiter, only show jobs created by the recruiter
        if current_user is not None and current_user.role == UserRole.RECRUITER:
            company = self._get_record_or_404(
                repository=self.company_repository,
                condition=Company.staff_id == current_user.user_id,
            )
            company_id = company.company_id
            condition = and_(condition, Job.company_id == company_id)
            jobs = self.job_repository.get_all(
                pagination=pagination, condition=condition, order_by=order_by
            )
        else:
            condition = and_(condition, Job.status > 0)
            jobs = self.job_repository.get_jobs_with_company(
                pagination=pagination, condition=condition, order_by=order_by
            )
        print("condition: ", condition)
        total = self.job_repository.count(condition=condition)
        job_details = {
            "total": total,
            "items": jobs,
        }
        return SuccessResponse(message=SuccessMessage.SUCCESS, data=job_details)

    async def update_job_details(
        self,
        staff_id,
        job_id,
        job_data,
        skills_data=None,
        certificates_data=None,
        educations_data=None,
    ):
        job = self._get_record_or_404(
            repository=self.job_repository, condition=Job.job_id == job_id
        )
        company = self._get_record_or_404(
            repository=self.company_repository, condition=Company.staff_id == staff_id
        )
        if job.company_id != company.company_id:
            raise CustomException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=ErrorMessage.FORBIDDEN,
            )
        job_data["company_id"] = company.company_id
        job = self.job_repository.update_by_id(job_id, job_data)
        update_skills = self._update_related_entities(
            job_id,
            "job_id",
            skills_data,
            self.job_skill_repository,
            JobSkill,
            "skill_id",
        )
        update_certificates = self._update_related_entities(
            job_id,
            "job_id",
            certificates_data,
            self.job_certificate_repository,
            JobCertificate,
            "certificate_id",
        )
        update_educations = self._update_related_entities(
            job_id,
            "job_id",
            educations_data,
            self.job_education_repository,
            JobEducation,
            "education_id",
        )
        job_details = JobDetailsResponse(
            job=job,
            skills=update_skills,
            certificates=update_certificates,
            educations=update_educations,
        )
        return SuccessResponse(message=SuccessMessage.UPDATED, data=job_details)

    def _build_job_search_condition(
        self,
        keyword,
        skills,
        company_id,
        city_id,
        working_arrangement,
        career_id,
        position_id,
    ):
        conditions = []

        if keyword:
            keyword_condition = ilike_search(Job, "title", keyword)
            conditions.append(keyword_condition)
        if skills:
            conditions.append(Job.job_id == JobSkill.job_id)
            conditions.append(JobSkill.skill_id.in_(skills))
        if city_id:
            conditions.append(Job.city_id == city_id)
        if working_arrangement:
            conditions.append(Job.working_arrangement == working_arrangement)
        if career_id:
            conditions.append(Job.career_id == career_id)
        if position_id:
            conditions.append(Job.position_id == position_id)
        if company_id:
            conditions.append(Job.company_id == company_id)

        # Use the utility function to combine conditions
        condition = combine_conditions(conditions)
        return condition
