from sqlalchemy.orm import Session

from app.models import MPosition
from .base import BaseRepository


class MPositionRepository(BaseRepository[MPosition]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=MPosition,
            column_id=MPosition.auto_id,
        )
