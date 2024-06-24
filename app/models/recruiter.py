from sqlalchemy import Column, Integer, String, Boolean

from app.models import Base

class Recruiter(Base):
    __tablename__ = "recruiters"

    recruiter_id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    email = Column(String(255), nullable=False)
    phone_number = Column(String(20))
    position_id = Column(String)
    office_phone = Column(String(20))
    office_email = Column(String(128))
    is_deleted = Column(Boolean, default=False, nullable=False)

    def get_context_string(self):
        return f"{self.recruiter_id}-{self.email}"