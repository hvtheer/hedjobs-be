from app.models import Application
from .base import BaseRepository


class ApplicationRepository(BaseRepository[Application]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=Application,
            column_id=Application.application_id,
        )
