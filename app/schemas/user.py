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

# class RegisterUserRequest(BaseModel):
#     name: str
#     email: EmailStr
#     password: str
#     role: str
    
    
class VerifyUserRequest(BaseModel):
    token: str
    email: EmailStr
    
class EmailRequest(BaseModel):
    email: EmailStr
    
class ResetRequest(BaseModel):
    token: str
    email: EmailStr
    password: str
    
    