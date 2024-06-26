from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from typing import Optional, List

from app.responses.base import SuccessResponse, Page
from app.responses.job import JobResponse, JobDetailsResponse
from app.schemas.job import JobDetailsRequest
from app.services.job import JobService
from app.config.security import require_role, get_current_user
from app.config.constants import UserRole
from app.config.database import get_session
from app.models import User, Job, JobSkill

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=SuccessResponse[JobDetailsResponse],
)
async def create_job(
    data: JobDetailsRequest,
    session: Session = Depends(get_session),
    current_user=Depends(require_role(UserRole.RECRUITER)),
):
    job_service = JobService(session)
    return await job_service.create_job_details(
        staff_id=current_user.user_id,
        job_data=data.job.dict(),
        skills_data=[skill.dict() for skill in data.skills],
        certificates_data=[certificate.dict() for certificate in data.certificates],
        educations_data=[education.dict() for education in data.educations],
    )


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=SuccessResponse[Page[JobResponse]],
)
async def get_jobs(
    session: Session = Depends(get_session),
    current_user: Optional[User] = Depends(get_current_user),
    keyword: Optional[str] = Query(None, description="Search job by keyword"),
    skills: Optional[List[int]] = Query(
        None, description="Search job by list of skills"
    ),
    company_id: Optional[int] = Query(None, description="Search job by company ID"),
    city_id: Optional[int] = Query(None, description="Search job by city ID"),
    working_arrangement: Optional[int] = Query(
        None, description="Search job by working arrangement"
    ),
    career_id: Optional[int] = Query(None, description="Search job by career ID"),
    position_id: Optional[int] = Query(None, description="Search job by position ID"),
    page: int = Query(1, description="Page number"),
    size: int = Query(10, description="Page size"),
):
    # test = session.query(Job).filter(JobSkill.skill_id.in_(skills)).all()
    # print(test)
    job_service = JobService(session)
    return await job_service.get_jobs(
        keyword=keyword,
        skills=skills,
        company_id=company_id,
        city_id=city_id,
        working_arrangement=working_arrangement,
        career_id=career_id,
        position_id=position_id,
        page=page,
        size=size,
        current_user=current_user,
    )


# @router.get(
#     "/",
#     status_code=status.HTTP_200_OK,
#     # response_model=SuccessResponse[List[JobDetailsResponse]],
# )
# async def get_jobs(
#     session: Session = Depends(get_session),
#     current_user=Depends(
#         require_role([UserRole.ADMIN, UserRole.RECRUITER, UserRole.STUDENT])
#     ),
#     keyword: Optional[str] = Query(None, description="Search job by keyword"),
#     skills: Optional[List[int]] = Query(
#         None, description="Search job by list of skills"
#     ),
#     city_id: Optional[int] = Query(None, description="Search job by city ID"),
#     working_arrangement: Optional[int] = Query(
#         None, description="Search job by working arrangement"
#     ),
#     career_id: Optional[int] = Query(None, description="Search job by career ID"),
#     position_id: Optional[int] = Query(None, description="Search job by position ID"),
#     page: int = Query(1, description="Page number"),
#     size: int = Query(10, description="Page size"),
# ):
#     print("current_use: %s" % current_user.user_id)
#     print(current_user.role)
#     job_service = JobService(session)
#     return await job_service.get_jobs(
#         keyword=keyword,
#         skills=skills,
#         city_id=city_id,
#         working_arrangement=working_arrangement,
#         career_id=career_id,
#         position_id=position_id,
#         page=page,
#         size=size,
#     )


@router.get(
    "/{job_id}",
    status_code=status.HTTP_200_OK,
    response_model=SuccessResponse[JobDetailsResponse],
)
async def get_job(job_id: int, session: Session = Depends(get_session)):
    job_service = JobService(session)
    return await job_service.get_job_by_id(job_id)
