from sqlalchemy.orm import Session
from sqlalchemy import and_

from app.models import Job
from .base import BaseRepository


class JobRepository(BaseRepository[Job]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=Job,
            column_id=Job.job_id,
        )

    # def get_jobs_active(self, pagination, condition, order_by):
    #     # condition = and_(Job.status > 0, condition)
    #     self.get_all(pagination, condition, order_by)
