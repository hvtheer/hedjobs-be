from sqlalchemy.orm import Session
from app.models import StudentEducation
from .base import BaseRepository


class StudentEducationRepository(BaseRepository[StudentEducation]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=StudentEducation,
            column_id=StudentEducation.auto_id,
        )
