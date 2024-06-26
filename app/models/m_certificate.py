from sqlalchemy import Column, Integer, String, UniqueConstraint
from app.models import Base


class MCertificate(Base):
    __tablename__ = "m_certificate"
    certificate_id = Column(Integer, primary_key=True, autoincrement=True)
    certificate_name = Column(String(150), nullable=False, default="")
