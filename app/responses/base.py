
from pydantic import BaseModel, ConfigDict
from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class BaseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

class InfoResponse(BaseModel):
    pass

class SuccessResponse(BaseModel, Generic[T]):
    message: str
    data: Optional[T] = None

class ErrorResponse(BaseModel):
    message: str