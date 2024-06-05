from sqlalchemy import Column, Integer, String, Date
from .base import BaseModel

class User(BaseModel):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(128), nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    phone_number = Column(String(20), nullable=False)
    date_of_birth = Column(Date)
    role_cd = Column(String(3), nullable=False)