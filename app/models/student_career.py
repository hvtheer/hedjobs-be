from sqlalchemy import Column, Integer, String, Date
from app.models import Base


class StudentCareer(Base):
    __tablename__ = "student_careers"

    auto_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer)
    career_id = Column(Integer)
    position_id = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    description = Column(String)
