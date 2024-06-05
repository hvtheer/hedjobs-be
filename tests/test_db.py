import pytest
from sqlalchemy import Column, Integer, String, select
from .conftest import Base, engine, db_session, SQLAlchemyError

class ExampleTable(Base):
    __tablename__ = 'example'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<ExampleTable(id={self.id}, name='{self.name}')>"

def test_can_connect(db_session):
    try:
        result = db_session.execute(select(1)).scalar()
        assert result == 1
    except SQLAlchemyError as e:
        pytest.fail(f"Database connection failed: {str(e)}")

def test_insert_into_example(db_session):
    try:
        # Insert a row into the example table
        new_row = ExampleTable(name="Test Name")
        db_session.add(new_row)
        db_session.commit()

        # Query the table to check the insertion
        result = db_session.query(ExampleTable).filter_by(name="Test Name").first()
        assert result is not None
        assert result.name == "Test Name"
    except SQLAlchemyError as e:
        pytest.fail(f"Insertion failed: {str(e)}")

def test_select_from_example(db_session):
    try:
        # Query the example table
        results = db_session.query(ExampleTable).all()
        assert len(results) > 0
    except SQLAlchemyError as e:
        pytest.fail(f"Selection failed: {str(e)}")

