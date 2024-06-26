from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from app.responses.base import ErrorResponse


class CustomException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)


async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(message=exc.detail).dict(),
    )
