# tests/conftest.py
import sys
import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

load_dotenv()

# Ensure the app directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Use a separate test database
TEST_DATABASE_URL = os.getenv("DATABASE_URL")

# Setting up the test database
engine = create_engine(TEST_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

@pytest.fixture(scope='session', autouse=True)
def setup_database():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database tables after the tests
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope='function')
def db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
