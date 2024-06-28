from typing import Union, Optional
from datetime import datetime
from pydantic import EmailStr

from .base import BaseResponse


class UserResponse(BaseResponse):
    user_id: int
    name: str
    email: EmailStr
    phone_number: Optional[str]
    is_active: bool
    role: str
    created_at: datetime


class LoginResponse(BaseResponse):
    access_token: str
    expires_in: int
    token_type: str = "Bearer"
