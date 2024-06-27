from sqlalchemy.orm import Session

from app.models import RateSkillMatching
from .base import BaseRepository


class RateSkillMatchingRepository(BaseRepository[RateSkillMatching]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=RateSkillMatching,
            column_id=RateSkillMatching.auto_id,
        )
