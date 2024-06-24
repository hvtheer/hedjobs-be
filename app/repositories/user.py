from sqlalchemy.orm import Session
from fastapi import status
from sqlalchemy import asc, desc
import logging
from sqlalchemy import Index, inspect, Column, Boolean, asc, desc
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Optional, Type, TypeVar, Generic, Dict, Any
from sqlalchemy.sql.elements import UnaryExpression



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
        condition = User.email == email
        order_by = asc(User.email)

        users = self.get_all(condition=condition,order_by=order_by)

        # users = self.get_all(condition=condition)

        for user in users:
            print(user.email)
        if not users:
            return None
        # print(users[0].email)
        return users[0]