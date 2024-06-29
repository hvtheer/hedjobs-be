from fastapi import APIRouter
from .auths import router as auths_router
from .users import router as users_router
from .companies import router as companies_router
from .jobs import router as jobs_router
from .students import router as students_router
from .applications import router as applications_router

router = APIRouter(prefix="/v1")

router.include_router(auths_router)
router.include_router(users_router)
router.include_router(companies_router)
router.include_router(jobs_router)
router.include_router(students_router)
router.include_router(applications_router)
# router.include_router(tiers_router)
# router.include_router(rate_limits_router)
