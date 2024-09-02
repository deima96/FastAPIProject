from unittest.mock import MagicMock
import pytest
from main import app,get_db

mock_session = MagicMock()

def override_getdb():
    try:
        yield mock_session
    finally:
        pass

app.dependency_overrides[get_db] = override_getdb()


@pytest.fixture
def mock_db_session():
    return mock_session