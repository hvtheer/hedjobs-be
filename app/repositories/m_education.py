from sqlalchemy.orm import Session

from app.models import MEducation
from .base import BaseRepository


class MEducationRepository(BaseRepository[MEducation]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=MEducation,
            column_id=MEducation.education_id,
        )
