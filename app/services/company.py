from fastapi import status
from sqlalchemy.orm import Session
from sqlalchemy import or_, func, asc, desc
from unidecode import unidecode

from app.models import Company
from app.services.base import BaseService
from app.responses.base import Page, SuccessResponse
from app.config.constants import ErrorMessage, SuccessMessage
from app.utils.exception import CustomException
from app.models.company import Company
from app.utils import *


class CompanyService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session)

    async def create_company(self, new_company, staff_id):
        ensure_unique_record(
            repository=self.company_repository, condition=Company.staff_id == staff_id
        )
        new_company["staff_id"] = staff_id
        company = self.company_repository.create(new_company)
        return SuccessResponse(message=SuccessMessage.CREATED, data=company)

    async def get_own_company(self, staff_id):
        company = get_record_or_404(
            repository=self.company_repository, condition=Company.staff_id == staff_id
        )
        return SuccessResponse(message=SuccessMessage.SUCCESS, data=company)

    async def get_company_by_id(self, company_id):
        company = get_record_or_404(
            repository=self.company_repository,
            condition=Company.company_id == company_id,
        )
        return SuccessResponse(message=SuccessMessage.SUCCESS, data=company)

    async def get_companies(self, name: str = None, page: int = None, size: int = None):
        condition = None
        if name:
            condition = ilike_search(Company, "name", name)
        order_by = [asc(Company.name), desc(Company.company_size)]
        pagination = {"page": page, "size": size}
        companies = self.company_repository.get_all(
            pagination=pagination, condition=condition, order_by=order_by
        )
        total = self.company_repository.count(condition=condition)
        data = Page(total=total, items=companies)
        return SuccessResponse(message=SuccessMessage.SUCCESS, data=data)
