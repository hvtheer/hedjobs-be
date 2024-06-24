from sqlalchemy import Column, Integer, String, SmallInteger, Date, Text
from app.models import Base

class Company(Base):
    __tablename__ = 'companies'

    company_id = Column(Integer, primary_key=True, autoincrement=True)
    staff_id = Column(Integer)
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