from pydantic import EmailStr
from datetime import date
from typing import Optional

from .base import BaseResponse


class CompanyResponse(BaseResponse):
    company_id: int
    name: str
    staff_id: int
    website: Optional[str] = None
    address: Optional[str] = None
    city_id: Optional[int] = None
    logo_url: Optional[str] = None
    established_in: Optional[date] = None
    contact_email: Optional[EmailStr] = None
    contact_phone: Optional[str] = None
    company_size: Optional[int] = None
    description: Optional[str] = None
