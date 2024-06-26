from sqlalchemy.orm import Session

from app.models import JobCertificate
from .base import BaseRepository


class JobCertificateRepository(BaseRepository[JobCertificate]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=JobCertificate,
            column_id=JobCertificate.job_certificate_id,
        )
