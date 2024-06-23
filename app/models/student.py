from sqlalchemy import Boolean, Column, DateTime, Integer, String, func, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from app.models import Base

class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone_number = Column(String(20))
    is_deleted = Column(Boolean, default=False, nullable=False)

    def get_context_string(self):
        return f"{self.email}".strip()
