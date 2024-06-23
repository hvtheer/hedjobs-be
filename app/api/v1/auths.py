from fastapi import APIRouter, BackgroundTasks, Depends, status, Header
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.config.database import get_session
from app.responses.user import UserResponse, LoginResponse
from app.responses.base import SuccessResponse
from app.schemas.user import RegisterUserRequest, ResetRequest, VerifyUserRequest, EmailRequest
from app.services import AuthService
from app.utils.exception import CustomException

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@router.post("/register", response_model=SuccessResponse[UserResponse])
async def register_user(data: RegisterUserRequest, background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
    auth_service = AuthService(session)
    return await auth_service.register(data.dict(), background_tasks)

@router.post("/verify", status_code=status.HTTP_200_OK)
async def verify_user_account(data: VerifyUserRequest, background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
    auth_service = AuthService(session)
    await auth_service.activate_user_account(data, background_tasks)
    return JSONResponse({"message": "Account is activated successfully."})

@router.post("/login", status_code=status.HTTP_200_OK, response_model=LoginResponse)
async def user_login(data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    auth_service = AuthService(session)
    return await auth_service.get_login_token(data)

# @router.post("/refresh", status_code=status.HTTP_200_OK, response_model=LoginResponse)
# async def refresh_token(refresh_token = Header(), session: Session = Depends(get_session)):
#     return await user.get_refresh_token(refresh_token, session)

# @router.post("/forgot-password", status_code=status.HTTP_200_OK)
# async def forgot_password(data: EmailRequest, background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
#     await user.email_forgot_password_link(data, background_tasks, session)
#     return JSONResponse({"message": "A email with password reset link has been sent to you."})

# @router.put("/reset-password", status_code=status.HTTP_200_OK)
# async def reset_password(data: ResetRequest, session: Session = Depends(get_session)):
#     await user.reset_user_password(data, session)
#     return JSONResponse({"message": "Your password has been updated."})