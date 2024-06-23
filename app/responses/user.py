from typing import Union, Optional
from datetime import datetime
from pydantic import EmailStr, BaseModel

from .base import BaseResponse

class UserBase(BaseResponse):
    name: str
    email: EmailStr
    phone_number: Optional[str]
    is_active: bool
    role: str

class UserResponse(UserBase):
    user_id: int
    # verified_at: Optional[datetime]
    # last_login_at: Optional[datetime]
    # read_last_notifications_at: datetime
    created_at: datetime
    # updated_at: Optional[datetime]

class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int
    token_type: str = "Bearer"