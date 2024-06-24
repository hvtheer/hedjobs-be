from sqlalchemy import Column, Integer, SmallInteger, String, Date, Text, Numeric, Boolean
from sqlalchemy.orm import validates
from sqlalchemy.event import listens_for
from datetime import date
from app.models import Base

class Job(Base):
    __tablename__ = 'jobs'

    job_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False, default='')
    company_id = Column(Integer, nullable=False, default=0)
    employment_type = Column(String(15), nullable=False, default='')
    salary_type = Column(String(2))
    min_salary = Column(Numeric(precision=13, scale=2))
    max_salary = Column(Numeric(precision=13, scale=2))
    currency_cd = Column(String(3))
    city_id = Column(SmallInteger)
    location = Column(String(255))
    working_arrangement = Column(String(15), nullable=False, default='')
    description = Column(Text)
    requirements = Column(Text)
    benefits = Column(Text)
    posted_date = Column(Date)
    closed_date = Column(Date)
    status = Column(SmallInteger, nullable=False, default=1)
    career_id = Column(Integer)
    position_id = Column(SmallInteger)
    interview_process = Column(Text)
    quantity = Column(SmallInteger)

    @validates('closed_date')
    def validate_closed_date(self, key, closed_date):
        if closed_date and closed_date <= date.today():
            self.status = 0
        return closed_date

@listens_for(Job, 'before_update')
def receive_before_update(mapper, connection, target):
    if target.closed_date and target.closed_date <= date.today():
        target.status = 0