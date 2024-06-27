from sqlalchemy import Column, Integer, String
from app.models import Base


class MCareer(Base):
    __tablename__ = "m_career"
    career_id = Column(Integer, primary_key=True, autoincrement=True)
    career_name = Column(String(150), nullable=False, default="")
