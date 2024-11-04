from fastapi.testclient import TestClient
from unittest.mock import MagicMock
import pytest
from main import app, create_user_in_db, get_user_from_db

client = TestClient(app)

@pytest.fixture
def mock_db():
    return MagicMock()

def test_create_user(mock_db, mocker):
    mock_user = MagicMock()
    mock_user.name = "Test User"
    mock_user.email = "test@example.com"
    mocker.patch('main.create_user_in_db', return_value={"name": "Test User", "email": "test@example.com"})
    response = client.post("/users", json={"name": "Test User", "email": "test@example.com"})
    assert response.status_code == 200
    assert response.json() == {"name": "Test User", "email": "test@example.com"}

def test_get_user(mock_db, mocker):
    mock_user = MagicMock()
    mock_user.name = "Test User"
    mock_user.email = "test@example.com"
    mocker.patch('main.get_user_from_db', return_value={"name": "Test User", "email": "test@example.com"})
    response = client.get("/users/test@example.com")
    assert response.status_code == 200
    assert response.json() == {"name": "Test User", "email": "test@example.com"}
    
def test_create_user_with_incorrect_expectation():
    response = client.post("/users", json={"name": "Wrong Name", "email": "test@example.com"})
    assert response.status_code == 200
    assert response.json() == {"name": "Test User", "email": "test@example.com"}
