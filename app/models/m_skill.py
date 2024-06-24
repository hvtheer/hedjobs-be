from sqlalchemy import Column, Integer, String, UniqueConstraint
from app.models import Base

class MSkill(Base):
    __tablename__ = 'm_skill'
    auto_id = Column(Integer, primary_key=True, autoincrement=True)
    skill_id = Column(Integer, nullable=False, default=0)
    skill_name = Column(String(150), nullable=False, default='')
    lang_code = Column(String(2), nullable=False, default='')
    __table_args__ = (UniqueConstraint('skill_id', 'lang_code'),)