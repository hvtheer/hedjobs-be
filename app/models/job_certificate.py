from sqlalchemy import Column, Integer, UniqueConstraint, ForeignKey
from app.models import Base


class JobCertificate(Base):
    __tablename__ = "job_certificates"

    job_certificate_id = Column(Integer, primary_key=True, autoincrement=True)
    certificate_id = Column(Integer)
    job_id = Column(Integer, ForeignKey("jobs.job_id"))

    __table_args__ = (UniqueConstraint("job_id", "certificate_id"),)
