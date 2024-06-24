from sqlalchemy.orm import Session

from app.models import JobEducation
from .base import BaseRepository

class JobEducationRepository(BaseRepository[JobEducation]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=JobEducation,
            column_id=JobEducation.job_education_id,
        )
