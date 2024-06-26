from sqlalchemy import Column, Integer, String
from app.models import Base


class StudentEducation(Base):
    __tablename__ = "student_educations"

    auto_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer)
    education_id = Column(Integer)
    education_organization_name = Column(String(255))
    major_name = Column(String(150))
    education_year = Column(Integer)
