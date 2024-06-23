from fastapi import APIRouter, BackgroundTasks, Depends, status, Header
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.config.database import get_session
from app.responses.auth import UserResponse, LoginResponse
from app.responses.base import SuccessResponse, InfoResponse
from app.schemas.auth import RegisterUserRequest, VerifyUserRequest
from app.services import AuthService
from app.utils.exception import CustomException
from app.config.constants import SuccessMessage

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=SuccessResponse[UserResponse])
async def register_user(data: RegisterUserRequest, background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
    auth_service = AuthService(session)
    return await auth_service.register(data.dict(), background_tasks)

@router.post("/verify", status_code=status.HTTP_200_OK)
async def verify_user_account(data: VerifyUserRequest, background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
    auth_service = AuthService(session)
    return await auth_service.activate_user_account(data.dict(), background_tasks)

@router.post("/login", status_code=status.HTTP_200_OK)
async def user_login(data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    auth_service = AuthService(session)
    return await auth_service.get_login_token(data)