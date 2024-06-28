from datetime import datetime, timedelta
import logging
from sqlalchemy.orm import Session
from fastapi import status
from typing import Dict, Any

from app.models import *
from .base import BaseService
from app.utils import *
from app.repositories import *
from app.config.constants import *
from app.config.settings import get_settings
from app.responses import *

settings = get_settings()


class UserService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session)

    async def get_all_users(self):
        users = self.user_repository.get_all(order_by=User.name)
        total_users = len(users)
        users = {"items": users, "total": total_users}
        return SuccessResponse(message=SuccessMessage.SUCCESS, data=users)

    # async def get_me(self, user_id):
    #     user = self.user_repository.get_by_id(user_id)
    #     return SuccessResponse(message=SuccessMessage.SUCCESS, data=user)
