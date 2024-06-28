from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models import *
from app.models.company import Company
from .base import BaseRepository


class JobRepository(BaseRepository[Job]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=Job,
            column_id=Job.job_id,
        )

    def get_jobs_with_company(self, pagination, condition, order_by):
        # Create a JOIN between Job, Company, and JobSkill tables
        query = self.session.query(Job, Company).join(
            Company, Job.company_id == Company.company_id
        )

        query_all = self._handle_get_all(query, pagination, condition, order_by)

        jobs_with_companies = []
        for job, company in query_all:
            job.company = company
            jobs_with_companies.append(job)
        return jobs_with_companies
