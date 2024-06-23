from sqlalchemy.orm import Session

from app.models.user import User
from .base import BaseRepository

class UserRepository(BaseRepository[User]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=User,
            column_id=User.user_id,
        )