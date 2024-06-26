from sqlalchemy import Boolean, Column, Integer, String

from app.models import Base


class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    email = Column(String(255), nullable=False)
    address = Column(String(255))
    phone_number = Column(String(20))
    is_deleted = Column(Boolean, default=False, nullable=False)

    def get_context_string(self):
        return f"{self.student_id}-{self.email}"
