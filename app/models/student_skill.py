from sqlalchemy import Column, Integer, ForeignKey
from app.models import Base


class StudentSkill(Base):
    __tablename__ = "student_skills"

    auto_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    skill_id = Column(Integer)
    skill_yoe = Column(Integer)
