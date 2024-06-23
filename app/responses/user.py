
from pydantic import EmailStr, BaseModel

from .base import BaseResponse

class UserResponse(BaseResponse):
    user_id: int
    name: str
    email: EmailStr
    phone_number: str
    role: str