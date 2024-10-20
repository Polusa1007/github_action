# test_advice_slip.py

import pytest
from login_setup import LoginSetUp

@pytest.fixture
def login_setup():
    """Fixture 初始化 LoginSetUp"""
    return LoginSetUp()

def test_get_advice(login_setup):
    """測試從 Advice Slip API 獲取建議"""
    response = login_setup.get_advice()
    
    # 檢查回應是否有正確的 'slip' 和 'advice' 字段
    assert 'slip' in response
    assert 'advice' in response['slip']
    
    print(f"Received advice: {response['slip']['advice']}")
