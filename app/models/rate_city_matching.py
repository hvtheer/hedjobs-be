from sqlalchemy import Column, Integer, Float
from .base import Base


class RateCityMatching(Base):
    __tablename__ = "rate_city_matching"

    auto_id = Column(Integer, primary_key=True, index=True)
    city_id1 = Column(Integer, index=True)
    city_id2 = Column(Integer, index=True)
    matching_rate = Column(Float)

    __table_args__ = (UniqueConstraint("city_id1", "city_id2"),)
