from sqlalchemy import Column, Integer, String
from app.models import Base


class StudentCareer(Base):
    __tablename__ = "student_careers"

    student_career_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer)
    career_id = Column(Integer)
    position_id = Column(Integer)
    description = Column(String)
