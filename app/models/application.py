from sqlalchemy import Column, Integer, SmallInteger, Float
from app.models import Base


class Application(Base):
    __tablename__ = "applications"

    application_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer)
    job_id = Column(Integer)
    stage_id = Column(SmallInteger, default=0)
    matching_score = Column(Float)
