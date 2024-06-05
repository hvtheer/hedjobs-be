from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import DATABASE_URL
from app.core.database import check_database_connection


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root_access():
    check_database_connection()
    return {"message": DATABASE_URL}
