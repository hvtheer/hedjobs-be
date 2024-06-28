from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.config.database import get_session
from app.responses import *
from app.config.security import require_role
from app.schemas import CompanyRequest
from app.services import CompanyService
from app.config.constants import UserRole

router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=SuccessResponse[CompanyResponse],
)
async def create_company(
    data: CompanyRequest,
    session: Session = Depends(get_session),
    current_user=Depends(require_role(UserRole.RECRUITER)),
):
    company_service = CompanyService(session)
    return await company_service.create_company(data.dict(), current_user.user_id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=SuccessResponse[Page[CompanyPublicResponse]],
)
async def get_companies(
    session: Session = Depends(get_session),
    name: Optional[str] = Query(None, description="Search company by name"),
    page: int = Query(1, description="Page number"),
    size: int = Query(10, description="Page size"),
):
    company_service = CompanyService(session)
    return await company_service.get_companies(name=name, page=page, size=size)


@router.get(
    "/me",
    status_code=status.HTTP_200_OK,
    response_model=SuccessResponse[CompanyResponse],
)
async def get_own_company(
    session: Session = Depends(get_session),
    user=Depends(require_role(UserRole.RECRUITER)),
):
    company_service = CompanyService(session)
    return await company_service.get_own_company(user.user_id)


@router.get(
    "/{company_id}",
    status_code=status.HTTP_200_OK,
    response_model=SuccessResponse[CompanyResponse],
)
async def get_company(company_id: int, session: Session = Depends(get_session)):
    company_service = CompanyService(session)
    return await company_service.get_company_by_id(company_id)
