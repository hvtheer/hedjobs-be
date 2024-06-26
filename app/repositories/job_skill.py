from sqlalchemy.orm import Session

from app.models import JobSkill
from .base import BaseRepository


class JobSkillRepository(BaseRepository[JobSkill]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=JobSkill,
            column_id=JobSkill.job_skill_id,
        )
