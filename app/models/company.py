from sqlalchemy import Column, Integer, String, SmallInteger, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.models import Base
from app.models.job import Job
from app.models.recruiter import Recruiter


class Company(Base):
    __tablename__ = "companies"

    company_id = Column(Integer, primary_key=True, autoincrement=True)
    recruiter_id = Column(Integer, ForeignKey("recruiters.recruiter_id"))
    name = Column(String(255), nullable=False)
    website = Column(String(100))
    address = Column(String(255))
    city_id = Column(SmallInteger)
    logo_url = Column(String(255))
    established_in = Column(Date)
    contact_email = Column(String(128))
    contact_phone = Column(String(20))
    company_size = Column(Integer)
    description = Column(Text)

    # Define the relationships
    jobs = relationship("Job", back_populates="company")
    recruiter = relationship("Recruiter", back_populates="company")
