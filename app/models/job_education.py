from sqlalchemy import Column, Integer, UniqueConstraint
from app.models import Base

class JobEducation(Base):
    __tablename__ = 'job_educations'

    job_education_id = Column(Integer, primary_key=True, autoincrement=True)
    education_id = Column(Integer)
    job_id = Column(Integer)

    __table_args__ = (UniqueConstraint('job_id', 'education_id'),)