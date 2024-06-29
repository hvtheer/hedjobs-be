from sqlalchemy import Column, Integer, UniqueConstraint, ForeignKey
from app.models import Base


class JobSkill(Base):
    __tablename__ = "job_skills"

    job_skill_id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer, ForeignKey("jobs.job_id"))
    skill_id = Column(Integer)
    skill_yoe = Column(Integer)

    __table_args__ = (UniqueConstraint("job_id", "skill_id"),)
