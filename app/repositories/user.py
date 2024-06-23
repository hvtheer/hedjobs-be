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

    def create_user(self, new_user):
        if self._email_exists(new_user['email']):
            raise CustomException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=ErrorMessage.ALREADY_EXISTS)
        new_user['password'] = self._hash_password(new_user['password'])
        return self.create(new_user)

    def _email_exists(self, email):
        return bool(self.get_all(condition={'email': email}))

    def _hash_password(self, password):
        return hash_password(password)