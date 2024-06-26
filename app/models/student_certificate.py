from sqlalchemy import Column, Integer
from app.models import Base


class StudentCertificate(Base):
    __tablename__ = "student_certificates"

    auto_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer)
    certificate_id = Column(Integer)
    certificate_year = Column(Integer)
