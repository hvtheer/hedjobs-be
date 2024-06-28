from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.config.database import get_session
from app.responses import *
from app.schemas.student import StudentDetailsRequest
from app.services.student import StudentService
from app.config.constants import UserRole
from app.config.security import require_role


router = APIRouter(
    prefix="/students",
    tags=["Students"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/me",
    status_code=status.HTTP_200_OK,
    response_model=SuccessResponse[StudentDetailsResponse],
)
async def get_self_student(
    session: Session = Depends(get_session),
    current_user=Depends(require_role(UserRole.STUDENT)),
):
    student_service = StudentService(session)
    return await student_service.get_self_student(current_user.user_id)


@router.get(
    "/{student_id}",
    status_code=status.HTTP_200_OK,
    response_model=SuccessResponse[StudentDetailsResponse],
)
async def get_student(student_id: int, session: Session = Depends(get_session)):
    student_service = StudentService(session)
    return await student_service.get_student_by_id(student_id)


@router.put(
    "/{student_id}",
    status_code=status.HTTP_201_CREATED,
    response_model=SuccessResponse[StudentDetailsResponse],
)
async def update_student(
    student_id: int,
    data: StudentDetailsRequest,
    session: Session = Depends(get_session),
    current_user=Depends(require_role(UserRole.STUDENT)),
):
    student_service = StudentService(session)
    return await student_service.update_student_details(
        user_id=current_user.user_id,
        student_id=student_id,
        student_data=data.student.dict(),
        skills_data=[skill.dict() for skill in data.skills],
        certificates_data=[certificate.dict() for certificate in data.certificates],
        educations_data=[education.dict() for education in data.educations],
        careers_data=[career.dict() for career in data.careers],
    )
