from sqlalchemy import Column, Integer, Float, UniqueConstraint
from .base import Base


class RateSkillMatching(Base):
    __tablename__ = "rate_skill_matching"

    auto_id = Column(Integer, primary_key=True, index=True)
    skill_id1 = Column(Integer, index=True)
    skill_id2 = Column(Integer, index=True)
    matching_rate = Column(Float)

    __table_args__ = (UniqueConstraint("skill_id1", "skill_id2"),)
