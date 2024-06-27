from sqlalchemy import Column, Integer, String
from app.models import Base


class MCity(Base):
    __tablename__ = "m_stage"
    stage_id = Column(Integer, primary_key=True, autoincrement=True)
    stage_name = Column(String(150), nullable=False, default="")
    stage_order = Column(Integer, nullable=False, default=0)
