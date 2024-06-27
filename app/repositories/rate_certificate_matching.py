from sqlalchemy.orm import Session

from app.models import RateCertificateMatching
from .base import BaseRepository


class RateCertificateMatchingRepository(BaseRepository[RateCertificateMatching]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=RateCertificateMatching,
            column_id=RateCertificateMatching.auto_id,
        )
