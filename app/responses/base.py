from pydantic import BaseModel, ConfigDict
from typing import TypeVar, Generic, Optional, List

M = TypeVar("M")


class BaseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class InfoResponse(BaseModel):
    message: str


class SuccessResponse(InfoResponse, Generic[M]):
    data: Optional[M] = None


class ErrorResponse(BaseModel):
    message: str


class Page(BaseResponse, Generic[M]):
    items: List[Optional[M]]
    total: int
