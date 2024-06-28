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

        # Apply condition, order_by, and pagination
        if condition is not None:
            query = query.filter(condition)
        if order_by is not None:
            query = query.order_by(order_by)
        if pagination:
            if "page" in pagination and "size" in pagination:
                page = pagination["page"]
                size = pagination["size"]
                query = query.offset((page - 1) * size).limit(size)

        # Fetch all records and return as a list of Job objects with company details and job skills
        jobs_with_company = []
        for job, company in query.all():
            job.company = company
            jobs_with_company.append(job)
        return jobs_with_company
