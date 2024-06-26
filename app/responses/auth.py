from typing import Union, Optional
from datetime import datetime
from pydantic import EmailStr

from .base import BaseResponse


class UserBase(BaseResponse):
    name: str
    email: EmailStr
    phone_number: Optional[str]
    is_active: bool
    role: str


class UserResponse(UserBase):
    user_id: int
    created_at: datetime


class LoginResponse(BaseResponse):
    access_token: str
    expires_in: int
    token_type: str = "Bearer"
