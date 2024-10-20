import pytest
import requests
from Login_setup import LoginSetUp

@pytest.fixture
def login_setup():
    """Fixture to initialize and return LoginSetUp instance with token."""
    login_setup = LoginSetUp()
    token = login_setup.login()
    return login_setup, token

def test_account_list_all(login_setup):
    """Test the account_list_all API."""
    login_setup_instance, token = login_setup
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = requests.get(f'{login_setup_instance.base_url}/account_list_all', headers=headers)
    assert response.status_code == 200  # 檢查返回的狀態碼是否是 200
    print(response.content)  # 可以進行進一步的斷言來檢查返回內容
