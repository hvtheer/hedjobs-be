from sqlalchemy import Column, Integer, String
from app.models import Base


class MEducation(Base):
    __tablename__ = "m_education"
    education_id = Column(Integer, primary_key=True, autoincrement=True)
    education_name = Column(String(150), nullable=False, default="")
    education_level = Column(Integer, nullable=False)
