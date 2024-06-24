from sqlalchemy import Column, Integer, UniqueConstraint
from app.models import Base


class JobCertificate(Base):
    __tablename__ = "job_certificates"

    job_certificate_id = Column(Integer, primary_key=True, autoincrement=True)
    certificate_id = Column(Integer)
    job_id = Column(Integer)

    __table_args__ = (UniqueConstraint("job_id", "certificate_id"),)
