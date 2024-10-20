# test_advice_slip.py

import pytest
import requests

def test_get_advice():
    """測試從 Advice Slip API 獲取建議"""
    base_url = "https://api.adviceslip.com/advice"
    response = requests.get(base_url)

    # 檢查 HTTP 狀態碼是否為 200
    assert response.status_code == 200, f"Failed with status code {response.status_code}"

    # 檢查回應內容
    data = response.json()
    assert 'slip' in data, "No 'slip' key in response"
    assert 'advice' in data['slip'], "No 'advice' key in 'slip'"

    print(f"Received advice: {data['slip']['advice']}")
