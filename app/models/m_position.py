from sqlalchemy import Column, Integer, String, UniqueConstraint
from app.models import Base


class MPosition(Base):
    __tablename__ = "m_position"
    auto_id = Column(Integer, primary_key=True, autoincrement=True)
    position_id = Column(Integer, nullable=False, default=0)
    position_name = Column(String(150), nullable=False, default="")
    lang_code = Column(String(2), nullable=False, default="")
    __table_args__ = (UniqueConstraint("position_id", "lang_code"),)
