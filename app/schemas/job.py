from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class JobSkillRequest(BaseModel):
    skill_id: int
    skill_yoe: Optional[int] = None


class JobCertificateRequest(BaseModel):
    certificate_id: int


class JobEducationRequest(BaseModel):
    education_id: int


class JobRequest(BaseModel):
    title: str
    company_id: int
    employment_type: str
    salary_type: Optional[str] = None
    min_salary: Optional[float] = None
    max_salary: Optional[float] = None
    currency_cd: Optional[str] = None
    city_id: Optional[int] = None
    location: Optional[str] = None
    working_arrangement: str
    description: Optional[str] = None
    requirements: Optional[str] = None
    benefits: Optional[str] = None
    posted_date: Optional[date] = None
    closed_date: Optional[date] = None
    status: str
    career_id: Optional[int] = None
    position_id: Optional[int] = None
    interview_process: Optional[str] = None
    quantity: Optional[int] = None


class JobDetailsRequest(BaseModel):
    job: Job
    skills: Optional[List[JobSkill]] = None
    certificates: Optional[List[JobCertificate]] = None
    educations: Optional[List[JobEducation]] = None
