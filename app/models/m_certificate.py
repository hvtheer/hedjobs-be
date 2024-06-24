from sqlalchemy import Column, Integer, String, UniqueConstraint
from app.models import Base

class MCertificate(Base):
    __tablename__ = 'm_certificate'
    auto_id = Column(Integer, primary_key=True, autoincrement=True)
    certificate_id = Column(Integer, nullable=False, default=0)
    certificate_name = Column(String(150), nullable=False, default='')
    lang_code = Column(String(2), nullable=False, default='')
    __table_args__ = (UniqueConstraint('certificate_id', 'lang_code'),)