
from pydantic import BaseModel, ConfigDict
from typing import TypeVar, Generic

T = TypeVar('T')

class BaseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

class ResponseBase(BaseModel):
    message: str

class SuccessResponse(BaseModel, Generic[T]):
    message: str
    data: T

class ErrorResponse(ResponseBase):
    pass