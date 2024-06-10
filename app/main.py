from fastapi import FastAPI
from app.api import user
from fastapi_sqlalchemy import DBSessionMiddleware
from starlette.middleware.cors import CORSMiddleware
from app.config.settings import get_settings

settings = get_settings()

def create_application():
    application = FastAPI()
    application.include_router(user.user_router)
    application.include_router(user.guest_router)
    application.include_router(user.auth_router)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URI)

    # application.include_router(router, prefix=settings.API_PREFIX)
    return application


app = create_application()


@app.get("/")
async def root():
    return {"message": "Hi, I am Describly. Awesome - Your setrup is done & working."}