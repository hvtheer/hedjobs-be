from sqlalchemy.orm import Session
from app.models import StudentCareer
from .base import BaseRepository


class StudentCareerRepository(BaseRepository[StudentCareer]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=StudentCareer,
            column_id=StudentCareer.auto_id,
        )
