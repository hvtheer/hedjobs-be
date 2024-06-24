from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.config.database import get_session
from app.responses.user import UserResponse
from app.responses.base import SuccessResponse
from app.services import UserService
from app.config.security import get_current_user, oauth2_scheme, require_role
from app.config.constants import SuccessMessage, UserRole
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
    # dependencies=[Depends(oauth2_scheme), Depends(get_current_user)]
)

@router.get("/me", status_code=status.HTTP_200_OK, response_model=SuccessResponse[UserResponse])
async def get_me(user = Depends(get_current_user)):
    return SuccessResponse(message=SuccessMessage.SUCCESS, data=user)


@router.get("/", status_code=status.HTTP_200_OK, response_model=SuccessResponse[List[UserResponse]])
async def get_users(session: Session = Depends(get_session)):
    user_service = UserService(session)
    users = await user_service.get_all_users()
    return SuccessResponse(message=SuccessMessage.SUCCESS, data=users)