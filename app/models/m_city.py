from sqlalchemy import Column, Integer, String
from app.models import Base


class MCity(Base):
    __tablename__ = "m_city"
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String(150), nullable=False, default="")
