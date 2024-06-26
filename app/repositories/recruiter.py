from sqlalchemy.orm import Session

from app.models import Recruiter
from .base import BaseRepository


class RecruiterRepository(BaseRepository[Recruiter]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=Recruiter,
            column_id=Recruiter.recruiter_id,
        )
