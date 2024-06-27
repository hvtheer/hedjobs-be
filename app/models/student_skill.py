from sqlalchemy import Column, Integer, UniqueConstraint
from app.models import Base


class StudentSkill(Base):
    __tablename__ = "student_skills"

    auto_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer)
    skill_id = Column(Integer)
    skill_yoe = Column(Integer)
