from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker,  declarative_base
from .config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def check_database_connection():
    try:
        with SessionLocal() as session:
            result = session.execute(select(1))
            if result.scalar() == 1:
                print("okay")
            else:
                print("Unexpected result:", result.scalar())
    except Exception as e:
        print("Error connecting to database:", str(e))
