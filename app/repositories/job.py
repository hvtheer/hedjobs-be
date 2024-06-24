from sqlalchemy.orm import Session

from app.models import Job
from .base import BaseRepository

class JobRepository(BaseRepository[Job]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=Job,
            column_id=Job.company_id,
        )
