from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date


class CompanyRequest(BaseModel):
    name: str
    website: Optional[str] = None
    address: Optional[str] = None
    city_id: Optional[int] = None
    logo_url: Optional[str] = None
    established_in: Optional[date] = None
    contact_email: Optional[EmailStr] = None
    contact_phone: Optional[str] = None
    company_size: Optional[int] = None
    description: Optional[str] = None
