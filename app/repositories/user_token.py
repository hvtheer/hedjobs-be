from sqlalchemy.orm import Session

from app.models.user import UserToken
from .base import BaseRepository

class UserTokenRepository(BaseRepository[UserToken]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=UserToken,
            column_id=UserToken.user_token_id,
        )

