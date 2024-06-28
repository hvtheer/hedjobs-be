from typing import Optional
from pydantic import BaseModel, EmailStr


class UserRequest(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    is_active: bool = False
    role: str


class RegisterUserRequest(UserRequest):
    password: str


class VerifyUserRequest(BaseModel):
    token: str
    email: EmailStr
