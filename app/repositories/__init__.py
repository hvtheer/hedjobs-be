from .base import BaseRepository
from .user import UserRepository
from .user_token import UserTokenRepository

from .student import StudentRepository
from .student_skill import StudentSkillRepository
from .student_certificate import StudentCertificateRepository
from .student_career import StudentCareerRepository
from .student_education import StudentEducationRepository

from .recruiter import RecruiterRepository
from .company import CompanyRepository
from .job import JobRepository
from .job_skill import JobSkillRepository
from .job_education import JobEducationRepository
from .job_certificate import JobCertificateRepository

from .m_education import MEducationRepository
from .m_stage import MStageRepository
from .m_position import MPositionRepository

from .rate_career_matching import RateCareerMatchingRepository
from .rate_skill_matching import RateSkillMatchingRepository
from .rate_city_matching import RateCityMatchingRepository
from .rate_certificate_matching import RateCertificateMatchingRepository
from .application import ApplicationRepository
