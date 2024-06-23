from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.config.database import get_session
from app.responses.auth import UserResponse
from app.responses.base import SuccessResponse
from app.services import UserService
from app.config.security import get_current_user, oauth2_scheme
from app.config.constants import SuccessMessage

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(oauth2_scheme), Depends(get_current_user)]
)

@router.get("/me", status_code=status.HTTP_200_OK, response_model=SuccessResponse[UserResponse])
async def fetch_user(user = Depends(get_current_user)):
    return SuccessResponse(SuccessMessage.SUCCESS, user)


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_user_info(id, session: Session = Depends(get_session)):
    return await user.fetch_user_detail(id, session)