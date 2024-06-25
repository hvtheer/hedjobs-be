# from elasticsearch import Elasticsearch
from fastapi import status
from sqlalchemy.orm import Session

from app.models import Job
from app.services.base import BaseService
from app.responses.base import Page, SuccessResponse
from app.config.constants import ErrorMessage, SuccessMessage
from app.utils.exception import CustomException


class JobService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session)
        # self.es = Elasticsearch()

    async def create_job_details(
        self,
        staff_id,
        job_data,
        skills_data=None,
        certificates_data=None,
        educations_data=None,
    ):
        company = self._get_company_by_staff_id(staff_id)
        job_data["company_id"] = company.company_id
        job = self.job_repository.create(job_data)
        if skills_data:
            self._create_job_skills(job.job_id, skills_data)
        if certificates_data:
            self._create_job_certificates(job.job_id, certificates_data)
        if educations_data:
            self._create_job_educations(job.job_id, educations_data)

        # # Index the job in Elasticsearch
        # self._index_job(job)

        return SuccessResponse(message=SuccessMessage.CREATED, data=job)

    def _get_company_by_staff_id(self, staff_id):
        company = self.company_repository.get_company_by_staff_id(staff_id)
        if not company:
            raise CustomException(
                status_code=status.HTTP_404_NOT_FOUND, detail=ErrorMessage.NOT_FOUND
            )
        return company

    def _create_job_skills(self, job_id, skills_data):
        for skill in skills_data:
            skill["job_id"] = job_id
            self.job_skill_repository.create(skill)

    def _create_job_certificates(self, job_id, certificates_data):
        for certificate in certificates_data:
            certificate["job_id"] = job_id
            self.job_certificate_repository.create(certificate)

    def _create_job_educations(self, job_id, educations_data):
        for education in educations_data:
            education["job_id"] = job_id
            self.job_education_repository.create(education)

    # def _index_job(self, job):
    #     body = {
    #         "title": job.title,
    #         "description": job.description,
    #         "location": job.location,
    #         "company": job.company.name,
    #         "skills": [skill.name for skill in job.skills],
    #         "certificates": [certificate.name for certificate in job.certificates],
    #         "educations": [education.degree for education in job.educations],
    #     }
    #     self.es.index(index="jobs", id=job.job_id, body=body)

    # async def search_jobs(self, query: str, page: int = 1, size: int = 10):
    #     body = {
    #         "query": {
    #             "multi_match": {
    #                 "query": query,
    #                 "fields": [
    #                     "title",
    #                     "description",
    #                     "location",
    #                     "company",
    #                     "skills",
    #                     "certificates",
    #                     "educations",
    #                 ],
    #             }
    #         },
    #         "from": (page - 1) * size,
    #         "size": size,
    #     }
    #     response = self.es.search(index="jobs", body=body)
    #     hits = response["hits"]["hits"]
    #     total = response["hits"]["total"]["value"]

    #     jobs = [hit["_source"] for hit in hits]
    #     return Page(items=jobs, total=total)
