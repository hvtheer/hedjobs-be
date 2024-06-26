from sqlalchemy.orm import Session
from app.models import StudentCertificate
from .base import BaseRepository


class StudentCertificateRepository(BaseRepository[StudentCertificate]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=StudentCertificate,
            column_id=StudentCertificate.auto_id,
        )
