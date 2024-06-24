from sqlalchemy.orm import Session
from fastapi import status

from app.models.user import User
from .base import BaseRepository
from app.utils.exception import CustomException
from app.config.constants import ErrorMessage
from app.config.security import hash_password

class UserRepository(BaseRepository[User]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=User,
            column_id=User.user_id,
        )

    def create(self, new_user):
        new_user['password'] = hash_password(new_user['password'])
        return super().create(new_user)
    
    def get_user_by_email(self, email):
        users = self.get_all(condition={'email': email})
        if not users:
            return None
        return users[0]