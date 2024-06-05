import pytest
from sqlalchemy import text
from app.core.database import SessionLocal

@pytest.mark.parametrize("query, expected", [(text("SELECT 1"), 1)])
def test_database_query(query, expected):
    session = SessionLocal()
    try:
        result = session.execute(query)
        fetched_result = result.fetchone()[0]
        assert fetched_result == expected
    finally:
        session.close()
