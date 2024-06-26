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
