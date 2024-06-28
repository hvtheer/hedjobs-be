from sqlalchemy.orm import Session

from app.models import MStage
from .base import BaseRepository


class MStageRepository(BaseRepository[MStage]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=MStage,
            column_id=MStage.stage_id,
        )
