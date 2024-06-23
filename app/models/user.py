from sqlalchemy import Boolean, Column, DateTime, Integer, String, func, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from app.models import Base

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    email = Column(String(255), nullable=False)
    phone_number = Column(String(20))
    password = Column(String(100))
    is_active = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False, nullable=False)
    verified_at = Column(DateTime)
    role = Column(String(3), nullable=False)
    last_login_at = Column(DateTime)
    read_last_notifications_at = Column(DateTime, nullable=False, default=func.now())

    def get_context_string(self, context: str):
        return f"{context}{self.password[-6:]}{self.updated_at.strftime('%m%d%Y%H%M%S')}".strip()
    

class UserToken(Base):
    __tablename__ = "user_tokens"
    user_token_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    access_key = Column(String(250), nullable=True, index=True, default=None)
    refresh_key = Column(String(250), nullable=True, index=True, default=None)
    expires_at = Column(DateTime, nullable=False)