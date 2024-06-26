from sqlalchemy import Column, Integer, String, UniqueConstraint
from app.models import Base


class MCity(Base):
    __tablename__ = "m_city"
    auto_id = Column(Integer, primary_key=True, autoincrement=True)
    city_id = Column(Integer, nullable=False, default=0)
    city_name = Column(String(150), nullable=False, default="")
    lang_code = Column(String(2), nullable=False, default="")
    __table_args__ = (UniqueConstraint("city_id", "lang_code"),)
