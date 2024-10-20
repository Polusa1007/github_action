# login_setup.py

import requests

class LoginSetUp:
    def __init__(self):
        self.base_url = "https://api.adviceslip.com"
    
    def get_advice(self):
        """模擬從 Advice Slip API 獲取建議"""
        api_url = f'{self.base_url}/advice'
        response = requests.get(api_url)
        if response.status_code != 200:
            raise Exception(f"Request failed with status code {response.status_code}")
        return response.json()

# 注意：這裡的 get_advice 函數是簡單調用API返回結果。
