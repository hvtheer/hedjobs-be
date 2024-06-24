from fastapi import status
from sqlalchemy.orm import Session

from app.models import Job
from app.services.base import BaseService
from app.responses.base import Page, SuccessResponse
from app.config.constants import ErrorMessage, SuccessMessage
from app.utils.exception import CustomException


class JobService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session)
