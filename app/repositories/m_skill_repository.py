from sqlalchemy.orm import Session

from app.models import MSkill
from .base import BaseRepository


class MSkillRepository(BaseRepository[MSkill]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=MSkill,
            column_id=MSkill.auto_id,
        )
