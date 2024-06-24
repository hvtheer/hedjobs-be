from sqlalchemy import Column, Integer, String, UniqueConstraint
from app.models import Base

class MCareer(Base):
    __tablename__ = 'm_career'
    auto_id = Column(Integer, primary_key=True, autoincrement=True)
    career_id = Column(Integer, nullable=False, default=0)
    career_name = Column(String(150), nullable=False, default='')
    lang_code = Column(String(2), nullable=False, default='')
    __table_args__ = (UniqueConstraint('career_id', 'lang_code'),)