from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.responses.base import SuccessResponse
from app.responses.job import JobDetailsResponse
from app.schemas.job import JobDetailsRequest
from app.services.job import JobService
from app.config.security import require_role
from app.config.constants import UserRole
from app.config.database import get_session

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
