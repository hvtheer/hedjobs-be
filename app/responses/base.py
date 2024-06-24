from pydantic import BaseModel, ConfigDict
from typing import TypeVar, Generic, Optional, List

T = TypeVar("T")


class BaseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class InfoResponse(BaseModel):
    message: str


class SuccessResponse(InfoResponse, Generic[T]):
    data: Optional[T] = None


class ErrorResponse(BaseModel):
    message: str


class Page(BaseModel, Generic[T]):
    items: List[T]
    total: int
