from fastapi import status
from sqlalchemy.orm import Session
from app.models import *
from app.services.base import BaseService
from app.responses.base import Page, SuccessResponse
from app.responses.job import JobDetailsResponse
from app.config.constants import ErrorMessage, SuccessMessage, UserRole
from app.utils.exception import CustomException
from sqlalchemy import desc
from app.utils import *


class ApplicationService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session)

    # async def create_application(self, student_id, job_id, application_data):
    #     application_data["student_id"] = student_id
    #     application_data["job_id"] = job_id
    #     application = self.application_repository.create(application_data)
    #     return SuccessResponse(message=SuccessMessage.CREATED, data=application)
