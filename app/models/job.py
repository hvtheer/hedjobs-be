from sqlalchemy import (
    Column,
    Integer,
    SmallInteger,
    String,
    Date,
    Text,
    Numeric,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import validates
from sqlalchemy.event import listens_for
from datetime import date
from app.models import Base


class Job(Base):
    __tablename__ = "jobs"

    job_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False, default="")
    company_id = Column(Integer, ForeignKey("company.company_id"))
    employment_type = Column(
        SmallInteger
    )  # 1: Full-time, 2: Part-time, 3: Contract, 4: Temporary, 5: Internship, 6: Freelance
    salary_type = Column(SmallInteger)  # 1: Min, 2: Max, 3: Min-Max, 4: Deal
    min_salary = Column(Integer)
    max_salary = Column(Integer)
    currency_cd = Column(String(3))  # USD, VND, JPY
    city_id = Column(SmallInteger)
    location = Column(String(255))
    working_arrangement = Column(SmallInteger)  # 1: Remote, 2: On-site, 3: Hybrid
    description = Column(Text)
    requirements = Column(Text)
    benefits = Column(Text)
    posted_date = Column(Date)
    closed_date = Column(Date)
    status = Column(
        SmallInteger, nullable=False, default=1
    )  # 0: Closed, 1: Open, 2: Featured
    career_id = Column(Integer)
    position_id = Column(SmallInteger)
    interview_process = Column(Text)
    quantity = Column(SmallInteger)

    # Define the back_populates on the Job side to complete the bidirectional relationship
    company = relationship("Company", back_populates="jobs")

    # Relationship with JobSkills
    job_skills = relationship("JobSkills", backref="job", cascade="all, delete-orphan")

    # Relationship with JobCertificates
    job_certificates = relationship(
        "JobCertificates", backref="job", cascade="all, delete-orphan"
    )

    # Relationship with JobEducations
    job_educations = relationship(
        "JobEducations", backref="job", cascade="all, delete-orphan"
    )

    @validates("closed_date")
    def validate_closed_date(self, key, closed_date):
        if closed_date and closed_date <= date.today():
            self.status = 0
        return closed_date


@listens_for(Job, "before_update")
def receive_before_update(mapper, connection, target):
    if target.closed_date and target.closed_date <= date.today():
        target.status = 0
