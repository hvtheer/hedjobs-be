from sqlalchemy import Column, Integer, String
from app.models import Base


class MSkill(Base):
    __tablename__ = "m_skill"
    skill_id = Column(Integer, primary_key=True, autoincrement=True)
    skill_name = Column(String(150), nullable=False, default="")
