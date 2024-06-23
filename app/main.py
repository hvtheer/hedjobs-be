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
    # application.include_router(user.user_router)
    # application.include_router(user.guest_router)
    # application.include_router(user.auth_router)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URI)
    application.add_exception_handler(CustomException, custom_exception_handler)

    # application.include_router(router, prefix=settings.API_PREFIX)
    return application


app = create_application()


# @app.get("/")
# async def root():
#     return {"message": "Hi, I am Wakwak from Hedjobs. Awesome - Your setup is done & working."}

# from fastapi import FastAPI
# from .routers import router
# from .models import Base, engine
# from .exceptions import custom_exception_handler, CustomException

# app = FastAPI()

# # Create the database tables
# Base.metadata.create_all(bind=engine)

# # Include the routers
# app.include_router(router)

# # Add custom exception handler
# app.add_exception_handler(CustomException, custom_exception_handler)
