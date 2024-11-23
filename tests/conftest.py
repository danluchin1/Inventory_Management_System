import pytest
from database import setup_database

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    setup_database()
