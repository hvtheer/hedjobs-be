import os
from functools import lru_cache
from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import quote_plus

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):

    # App
    APP_NAME:  str = os.environ.get("APP_NAME", "HEDJOBS")
    DEBUG: bool = bool(os.environ.get("DEBUG", False))
    
    # FrontEnd Application
    FRONTEND_HOST: str = os.environ.get("FRONTEND_HOST", "http://localhost:3000")

    # MySql Database Config
    POSTGRES_HOST: str = os.environ.get("POSTGRES_HOST", 'postgres')
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER", 'postgres')
    POSTGRES_PASS: str = os.environ.get("POSTGRES_PASSWORD", 'postgres')
    POSTGRES_PORT: int = int(os.environ.get("POSTGRES_PORT", 5432))
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB", 'fastapi')
    DATABASE_URI: str = f"postgresql+psycopg2://{POSTGRES_USER}:%s@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}" % quote_plus(POSTGRES_PASS)

    # JWT Secret Key
    JWT_SECRET: str = os.environ.get("JWT_SECRET", "649fb93ef34e4fdf4187709c84d643dd61ce730d91856418fdcf563f895ea40f")
    JWT_ALGORITHM: str = os.environ.get("ACCESS_TOKEN_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 3))
    REFRESH_TOKEN_EXPIRE_MINUTES: int = int(os.environ.get("REFRESH_TOKEN_EXPIRE_MINUTES", 1440))

    # App Secret Key
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "8deadce9449770680910741063cd0a3fe0acb62a8978661f421bbcbb66dc41f1")


@lru_cache()
def get_settings() -> Settings:
    return Settings()
