from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class StudentSkillRequest(BaseModel):
    skill_id: int
    skill_yoe: int


class StudentEducationRequest(BaseModel):
    education_id: int
    education_organization_name: Optional[str]
    major_name: Optional[str]
    education_year: Optional[int]


class StudentCertificateRequest(BaseModel):
    certificate_id: int
    certificate_year: Optional[int]


class StudentCareerRequest(BaseModel):
    career_id: int
    position_id: int
    start_date: Optional[date]
    end_date: Optional[date]
    description: Optional[str]


class StudentRequest(BaseModel):
    name: str
    email: str
    address: Optional[str]
    phone_number: Optional[str]
    is_deleted: bool
    expected_city_id: Optional[int]
    expected_salary: Optional[int]


class StudentDetailsRequest(BaseModel):
    student: StudentRequest
    skills: Optional[List[StudentSkillRequest]]
    educations: Optional[List[StudentEducationRequest]]
    certificates: Optional[List[StudentCertificateRequest]]
    careers: Optional[List[StudentCareerRequest]]
