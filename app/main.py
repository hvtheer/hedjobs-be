from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from starlette.middleware.cors import CORSMiddleware

from app.api import router
from app.config.settings import get_settings
from app.utils.exception import CustomException, custom_exception_handler

settings = get_settings()


def create_application():
    application = FastAPI()
    application.include_router(router)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URI)
    application.add_exception_handler(CustomException, custom_exception_handler)

    return application


app = create_application()
