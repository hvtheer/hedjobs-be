from sqlalchemy.orm import Session

from app.models import MCity
from .base import BaseRepository


class MCityRepository(BaseRepository[MCity]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=MCity,
            column_id=MCity.city_id,
        )
