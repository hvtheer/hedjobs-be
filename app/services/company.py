from fastapi import status
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

from app.models import Company
from app.services import *
from app.responses import *
from app.config.constants import *
from app.utils import *
from app.models import *
from app.utils import *


class CompanyService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session)

    async def create_company(self, new_company, staff_id):
        self._ensure_unique_record(
            repository=self.company_repository, condition=Company.staff_id == staff_id
        )
        new_company["staff_id"] = staff_id
        company = self.company_repository.create(new_company)
        return SuccessResponse(message=SuccessMessage.CREATED, data=company)

    async def get_own_company(self, staff_id):
        company = self._get_record_or_404(
            repository=self.company_repository, condition=Company.staff_id == staff_id
        )
        return SuccessResponse(message=SuccessMessage.SUCCESS, data=company)

    async def get_company_by_id(self, company_id):
        company = self._get_record_or_404(
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
