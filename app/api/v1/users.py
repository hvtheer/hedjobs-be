from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.config.database import get_session
from app.responses import *
from app.services import UserService
from app.config.security import get_current_user, oauth2_scheme, require_role
from app.config.constants import SuccessMessage, UserRole

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/me", status_code=status.HTTP_200_OK, response_model=SuccessResponse[UserResponse]
)
async def get_me(user=Depends(get_current_user)):
    return SuccessResponse(message=SuccessMessage.SUCCESS, data=user)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=SuccessResponse[Page[UserResponse]],
)
async def get_users(session: Session = Depends(get_session)):
    user_service = UserService(session)
    return await user_service.get_all_users()
