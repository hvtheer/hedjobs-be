from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from app.models import Base


class StudentCareer(Base):
    __tablename__ = "student_careers"

    auto_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    career_id = Column(Integer)
    position_id = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    description = Column(String)

    @hybrid_property
    def duration_of_work(self):
        if self.start_date and self.end_date:
            duration = (self.end_date - self.start_date).days / 365
            return round(duration, 2)
        return None
