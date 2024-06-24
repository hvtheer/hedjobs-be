from sqlalchemy import Column, Integer, String, UniqueConstraint
from app.models import Base

class MEducation(Base):
    __tablename__ = 'm_education'
    auto_id = Column(Integer, primary_key=True, autoincrement=True)
    education_id = Column(Integer, nullable=False, default=0)
    education_name = Column(String(150), nullable=False, default='')
    lang_code = Column(String(2), nullable=False, default='')
    __table_args__ = (UniqueConstraint('education_id', 'lang_code'),)