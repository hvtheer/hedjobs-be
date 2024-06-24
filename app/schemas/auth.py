from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    is_active: bool = False
    role: str


class RegisterUserRequest(UserBase):
    password: str


class VerifyUserRequest(BaseModel):
    token: str
    email: EmailStr
