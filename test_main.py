# test_main.py
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
import pytest
from main import app, create_user_in_db, get_user_from_db

client = TestClient(app)

# 測試 fixture 模擬資料庫 session
@pytest.fixture
def mock_db():
    # 建立一個模擬的資料庫 session
    return MagicMock()

# 測試用戶創建 API
def test_create_user(mock_db, mocker):
    # 建立模擬的用戶對象
    mock_user = MagicMock()
    mock_user.name = "Test User"
    mock_user.email = "test@example.com"

    # 模擬 create_user_in_db 函數，讓它回傳 mock_user
    mocker.patch('main.create_user_in_db', return_value=mock_user)

    # 發送 POST 請求，模擬創建用戶
    response = client.post("/users", json={"name": "Test User", "email": "test@example.com"})

    # 確認返回的 HTTP 狀態碼和數據
    assert response.status_code == 200
    assert response.json() == {"name": "Test User", "email": "test@example.com"}

    # 確認 create_user_in_db 被正確呼叫
    create_user_in_db.assert_called_once_with(mock_db, mock_user)

# 測試用戶查詢 API
def test_get_user(mock_db, mocker):
    # 模擬從資料庫查詢用戶
    mock_user = MagicMock()
    mock_user.name = "Test User"
    mock_user.email = "test@example.com"

    # 模擬 get_user_from_db 函數回傳 mock_user
    mocker.patch('main.get_user_from_db', return_value=mock_user)

    # 發送 GET 請求查詢用戶
    response = client.get("/users/test@example.com")

    # 確認返回的 HTTP 狀態碼和數據
    assert response.status_code == 200
    assert response.json() == {"name": "Test User", "email": "test@example.com"}

    # 確認 get_user_from_db 被正確呼叫
    get_user_from_db.assert_called_once_with(mock_db, "test@example.com")
