from sqlalchemy import Column, Integer, UniqueConstraint
from app.models import Base


class JobSkill(Base):
    __tablename__ = "job_skills"

    job_skill_id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer, nullable=False, default=0)
    skill_id = Column(Integer, nullable=False, default=0)
    skill_yoe = Column(Integer)

    __table_args__ = (UniqueConstraint("job_id", "skill_id"),)
