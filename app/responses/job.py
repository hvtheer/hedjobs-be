from typing import List, Optional
from datetime import date
from .base import BaseResponse
from .company import CompanyPublicResponse


class JobSkillResponse(BaseResponse):
    skill_id: int
    skill_yoe: Optional[int] = None


class JobCertificateResponse(BaseResponse):
    certificate_id: int


class JobEducationResponse(BaseResponse):
    education_id: int


class JobResponse(BaseResponse):
    job_id: int
    title: str
    company_id: int
    employment_type: int
    salary_type: Optional[int] = None
    min_salary: Optional[int] = None
    max_salary: Optional[int] = None
    currency_cd: Optional[str] = None
    city_id: Optional[int] = None
    location: Optional[str] = None
    working_arrangement: int
    description: Optional[str] = None
    requirements: Optional[str] = None
    benefits: Optional[str] = None
    posted_date: Optional[date] = None
    closed_date: Optional[date] = None
    status: int
    career_id: Optional[int] = None
    position_id: Optional[int] = None
    interview_process: Optional[str] = None
    quantity: Optional[int] = None


class JobPublicResponse(BaseResponse):
    job_id: int
    title: str
    company: CompanyPublicResponse
    employment_type: int
    salary_type: Optional[int] = None
    min_salary: Optional[int] = None
    max_salary: Optional[int] = None
    currency_cd: Optional[str] = None
    city_id: Optional[int] = None
    posted_date: Optional[date] = None
    closed_date: Optional[date] = None
    status: int
    career_id: Optional[int] = None
    position_id: Optional[int] = None


class JobDetailsResponse(BaseResponse):
    job: JobResponse
    company: CompanyPublicResponse
    skills: Optional[List[JobSkillResponse]] = None
    certificates: Optional[List[JobCertificateResponse]] = None
    educations: Optional[List[JobEducationResponse]] = None
