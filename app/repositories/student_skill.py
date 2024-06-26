from sqlalchemy.orm import Session
from app.models import StudentSkill
from .base import BaseRepository


class StudentSkillRepository(BaseRepository[StudentSkill]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=StudentSkill,
            column_id=StudentSkill.auto_id,
        )
