from fastapi import status
from sqlalchemy.orm import Session

from .base import BaseService
from app.responses import *
from app.models import *
from app.utils import *
from app.config.constants import *


class ApplicationService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session)

    # async def create_application(self, student_id, job_id, application_data):
    #     application_data["student_id"] = student_id
    #     application_data["job_id"] = job_id
    #     application = self.application_repository.create(application_data)
    #     return SuccessResponse(message=SuccessMessage.CREATED, data=application)
