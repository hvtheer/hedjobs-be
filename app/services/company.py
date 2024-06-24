from fastapi import status
from sqlalchemy.orm import Session
from sqlalchemy import or_, func, asc
from unidecode import unidecode

from app.models import Company
from app.services.base import BaseService
from app.responses.base import Page, SuccessResponse
from app.config.constants import ErrorMessage, SuccessMessage
from app.utils.exception import CustomException
from app.models.company import Company

class CompanyService(BaseService):

    def __init__(self, session: Session):
        super().__init__(session)
    
    async def create_company(self, new_company, staff_id):
        if self.company_repository.get_company_by_staff_id(staff_id):
                raise CustomException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=ErrorMessage.ALREADY_EXISTS)
        new_company['staff_id'] = staff_id
        company = self.company_repository.create(new_company)
        return SuccessResponse(message=SuccessMessage.CREATED, data=company) 

    async def get_own_company(self, staff_id):
        company = self.company_repository.get_company_by_staff_id(staff_id)
        if not company:
            raise CustomException(status_code=status.HTTP_404_NOT_FOUND, detail=ErrorMessage.NOT_FOUND)
        return SuccessResponse(message=SuccessMessage.SUCCESS, data=company)
    
    async def get_company_by_id(self, company_id):
        company = self.company_repository.get_by_id(company_id)
        if not company:
            raise CustomException(status_code=status.HTTP_404_NOT_FOUND, detail=ErrorMessage.NOT_FOUND)
        return SuccessResponse(message=SuccessMessage.SUCCESS, data=company)

    async def get_companies(self, name: str = None, page: int = None, size: int = None):
        condition = None
        if name:
            condition = or_(
                func.unaccent(Company.name).ilike(f"%{name.lower()}%"),
                func.lower(Company.name).ilike(f"%{unidecode(name.lower())}%"),
            )
        order_by = asc(Company.name)
        pagination = {"page": page, "size": size}
        companies = self.company_repository.get_all(pagination=pagination, condition=condition, order_by=order_by)
        total = self.company_repository.count(condition=condition)
        return Page(total=total, items=companies)