from sqlalchemy.orm import Session

from app.models import Company
from .base import BaseRepository

class CompanyRepository(BaseRepository[Company]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=Company,
            column_id=Company.company_id,
        )

    def get_company_by_staff_id(self, staff_id):
        companies = self.get_all(condition={'staff_id': staff_id})
        if not companies:
            return None
        return companies[0]
