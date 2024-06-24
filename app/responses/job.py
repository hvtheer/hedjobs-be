from typing import List, Optional
from datetime import date

from .base import BaseResponse


class JobSkillResponse(BaseResponse):
    job_skill_id: int
    skill_id: int
    skill_yoe: Optional[int] = None


class JobCertificateResponse(BaseResponse):
    job_certificate_id: int
    certificate_id: int


class JobEducationResponse(BaseResponse):
    job_education_id: int
    education_id: int


class JobResponse(BaseResponse):
    job_id: int
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


class JobDetailsResponse(BaseResponse):
    job: Job
    skills: Optional[List[JobSkill]] = None
    certificates: Optional[List[JobCertificate]] = None
    educations: Optional[List[JobEducation]] = None
