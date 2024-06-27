from typing import List, Optional
from datetime import date

from .base import BaseResponse


class StudentSkillResponse(BaseResponse):
    skill_id: int
    skill_yoe: int


class StudentEducationResponse(BaseResponse):
    education_id: int
    education_organization_name: Optional[str]
    major_name: Optional[str]
    education_year: Optional[int]


class StudentCertificateResponse(BaseResponse):
    certificate_id: int
    certificate_year: Optional[int]


class StudentCareerResponse(BaseResponse):
    career_id: int
    position_id: int
    start_date: Optional[date]
    end_date: Optional[date]
    description: Optional[str]


class StudentResponse(BaseResponse):
    student_id: int
    name: str
    email: str
    address: Optional[str]
    phone_number: Optional[str]
    is_deleted: bool
    expected_city_id: Optional[int]
    expected_salary: Optional[int]


class StudentDetailsResponse(BaseResponse):
    student: StudentResponse
    skills: Optional[List[StudentSkillResponse]]
    certificates: Optional[List[StudentCertificateResponse]]
    educations: Optional[List[StudentEducationResponse]]
    careers: Optional[List[StudentCareerResponse]]
