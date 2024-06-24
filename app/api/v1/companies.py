from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.config.database import get_session
from app.responses.base import SuccessResponse
from app.responses.user import UserResponse
from app.responses.company import CompanyResponse
from app.config.security import get_current_user, oauth2_scheme, require_role
from app.schemas.company import CompanyRequest
from app.services.company import CompanyService
from app.config.constants import SuccessMessage, UserRole


router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
    responses={404: {"description": "Not found"}},
    # dependencies=[Depends(oauth2_scheme), Depends(get_current_user)]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SuccessResponse[CompanyResponse])
async def create_company(data: CompanyRequest, session: Session = Depends(get_session), current_user = Depends(require_role(UserRole.ADMIN, UserRole.RECRUITER))):
    company_service = CompanyService(session)
    return await company_service.create_company(data.dict(), current_user.user_id)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_companies(session: Session = Depends(get_session)):
    company_service = CompanyService(session)
    return await company_service.get_all_companies()

@router.get("/me", status_code=status.HTTP_200_OK, response_model=SuccessResponse[CompanyResponse])
async def get_own_company(session: Session = Depends(get_session), user = Depends(require_role(UserRole.RECRUITER))):
    company_service = CompanyService(session)
    return await company_service.get_own_company(user.user_id)

@router.get("/{company_id}", status_code=status.HTTP_200_OK, response_model=SuccessResponse[CompanyResponse])
async def get_company(company_id: int, session: Session = Depends(get_session)):
    company_service = CompanyService(session)
    return await company_service.get_company_by_id(company_id)
