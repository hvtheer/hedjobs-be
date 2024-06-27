from sqlalchemy.orm import Session

from app.models import RateCityMatching
from .base import BaseRepository


class RateCityMatchingRepository(BaseRepository[RateCityMatching]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=RateCityMatching,
            column_id=RateCityMatching.auto_id,
        )
