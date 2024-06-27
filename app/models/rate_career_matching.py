from sqlalchemy import Column, Integer, Float
from .base import Base


class CareerMatchingRate(Base):
    __tablename__ = "rate_career_matching"

    auto_id = Column(Integer, primary_key=True, index=True)
    career_id1 = Column(Integer, index=True)
    career_id2 = Column(Integer, index=True)
    matching_rate = Column(Float)

    __table_args__ = (UniqueConstraint("career_id1", "career_id2"),)
