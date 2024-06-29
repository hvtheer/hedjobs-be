from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from typing import Optional, List

from app.responses import *
from app.schemas import *
from app.services import ApplicationService
from app.config.security import require_role, get_current_user
from app.config.constants import UserRole
from app.config.database import get_session
from app.models import *


router = APIRouter(
    prefix="/applications",
    tags=["Applications"],
    responses={404: {"description": "Not found"}},
)


# @router.post(
#     "/",
#     status_code=status.HTTP_201_CREATED,
#     response_model=SuccessResponse[ApplicationDetailsResponse],
# )
# async def create_application(
#     data: ApplicationDetailsRequest,
#     session: Session = Depends(get_session),
#     current_user=Depends(require_role(UserRole.RECRUITER)),
# ):
#     application_service = ApplicationService(session)
#     return await application_service.create_application_details(
#         recruiter_id=current_user.user_id,
#         application_data=data.application.dict(),
#         skills_data=[skill.dict() for skill in data.skills],
#         certificates_data=[certificate.dict() for certificate in data.certificates],
#         educations_data=[education.dict() for education in data.educations],
#     )


# @router.put(
#     "/{application_id}",
#     status_code=status.HTTP_201_CREATED,
#     response_model=SuccessResponse[ApplicationDetailsResponse],
# )
# async def update_application(
#     application_id: int,
#     data: ApplicationDetailsRequest,
#     session: Session = Depends(get_session),
#     current_user=Depends(require_role(UserRole.RECRUITER)),
# ):
#     application_service = ApplicationService(session)
#     return await application_service.update_application_details(
#         recruiter_id=current_user.user_id,
#         application_id=application_id,
#         application_data=data.application.dict(),
#         skills_data=[skill.dict() for skill in data.skills],
#         certificates_data=[certificate.dict() for certificate in data.certificates],
#         educations_data=[education.dict() for education in data.educations],
#     )


# @router.get(
#     "/",
#     status_code=status.HTTP_200_OK,
#     response_model=SuccessResponse[Page[ApplicationPublicResponse]],
# )
# async def get_applications(
#     session: Session = Depends(get_session),
#     current_user: Optional[User] = Depends(get_current_user),
#     keyword: Optional[str] = Query(None, description="Search application by keyword"),
#     skills: Optional[List[int]] = Query(
#         None, description="Search application by list of skills"
#     ),
#     company_id: Optional[int] = Query(None, description="Search application by company ID"),
#     city_id: Optional[int] = Query(None, description="Search application by city ID"),
#     working_arrangement: Optional[int] = Query(
#         None, description="Search application by working arrangement"
#     ),
#     career_id: Optional[int] = Query(None, description="Search application by career ID"),
#     position_id: Optional[int] = Query(None, description="Search application by position ID"),
#     page: int = Query(1, description="Page number"),
#     size: int = Query(10, description="Page size"),
# ):
#     application_service = ApplicationService(session)
#     return await application_service.get_applications(
#         keyword=keyword,
#         skills=skills,
#         company_id=company_id,
#         city_id=city_id,
#         working_arrangement=working_arrangement,
#         career_id=career_id,
#         position_id=position_id,
#         page=page,
#         size=size,
#         current_user=current_user,
#     )


@router.get(
    "/me",
    status_code=status.HTTP_200_OK,
    # response_model=SuccessResponse[ApplicationDetailsResponse],
)
async def get_application(session: Session = Depends(get_session)):
    application_service = ApplicationService(session)
    return await application_service.create_application()
