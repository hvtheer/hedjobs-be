from sqlalchemy.orm import Session

from app.models import Student
from .base import BaseRepository


class StudentRepository(BaseRepository[Student]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=Student,
            column_id=Student.student_id,
        )
