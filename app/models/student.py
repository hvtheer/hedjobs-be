from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from app.models import Base


class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    email = Column(String(255), nullable=False)
    address = Column(String(255))
    phone_number = Column(String(20))
    is_deleted = Column(Boolean, default=False, nullable=False)
    expected_city_id = Column(Integer)
    expected_salary = Column(Integer)

    # Relationship with StudentSkills
    skills = relationship(
        "StudentSkills", backref="student", cascade="all, delete-orphan"
    )

    # Relationship with StudentEducations
    educations = relationship(
        "StudentEducations", backref="student", cascade="all, delete-orphan"
    )

    # Relationship with StudentCertificates
    certificates = relationship(
        "StudentCertificates", backref="student", cascade="all, delete-orphan"
    )

    # Relationship with StudentCareers
    careers = relationship(
        "StudentCareers", backref="student", cascade="all, delete-orphan"
    )

    def get_context_string(self):
        return f"{self.student_id}-{self.email}"
