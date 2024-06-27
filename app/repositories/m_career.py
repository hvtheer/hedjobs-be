from sqlalchemy.orm import Session

from app.models import MCareer
from .base import BaseRepository


class MCareerRepository(BaseRepository[MCareer]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=MCareer,
            column_id=MCareer.career_id,
        )
