from sqlalchemy import Column, Integer, Float, UniqueConstraint
from .base import Base


class RateCertificateMatching(Base):
    __tablename__ = "rate_certificate_matching"

    auto_id = Column(Integer, primary_key=True, index=True)
    certificate_id1 = Column(Integer, index=True)
    certificate_id2 = Column(Integer, index=True)
    matching_rate = Column(Float)

    __table_args__ = (UniqueConstraint("certificate_id1", "certificate_id2"),)
