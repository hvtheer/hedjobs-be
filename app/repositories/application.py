from app.models import Application
from .base import BaseRepository


class ApplicationRepository(BaseRepository[Application]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model=Application,
            column_id=Application.application_id,
        )

    def create_application(self, student, job, application_data):
        application_data["student_id"] = student.student_id
        application_data["job_id"] = job.job_id
        application_data["matching_rate"] = calculate_matching_rate(student, job)
        application = self.create(application_data)
        return application
