from sqlalchemy.orm import Session

from app.models import RateCareerMatching
from .base import BaseRepository


class RateCareerMatchingRepository(BaseRepository[RateCareerMatching]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=RateCareerMatching,
            column_id=RateCareerMatching.auto_id,
        )
