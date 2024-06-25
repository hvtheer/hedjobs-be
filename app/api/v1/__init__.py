from fastapi import APIRouter
from .auths import router as auths_router
from .users import router as users_router
from .companies import router as companies_router
from .jobs import router as jobs_router

router = APIRouter(prefix="/v1")

router.include_router(auths_router)
router.include_router(users_router)
router.include_router(companies_router)
router.include_router(jobs_router)
# router.include_router(posts_router)
# router.include_router(tasks_router)
# router.include_router(tiers_router)
# router.include_router(rate_limits_router)
