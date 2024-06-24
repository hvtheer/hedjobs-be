from fastapi import APIRouter, status
from app.responses.base import SuccessResponse
from app.responses.job import JobDetailsResponse
from app.schemas.job import JobDetailsRequest

router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SuccessResponse[JobDetailsResponse])
async def create_job(data: JobDetailsRequest, session: Session = Depends(get_session), current_user = Depends(require_role(UserRole.RECRUITER))):
    job_service = JobService(session)
    return await job_service.create_job(data.dict(), current_user.user_id)
