from sqlalchemy import Column, Integer, Date, Text
from app.models import Base


class JobApplication(Base):
    __tablename__ = "applications"

    application_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer)
    job_id = Column(Integer)
    stage_id = Column(SmallInteger, default=0)
    matching_score = Column(Float)
