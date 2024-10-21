# test_advice_slip.py

import pytest
import requests

def test_get_advice():
    base_url = "https://api.adviceslip.com/advice"
    response = requests.get(base_url)
    assert response.status_code == 200, f"Failed with status code {response.status_code}"

    data = response.json()
    assert 'slip' in data, "No 'slip' key in response"
    assert 'advice' in data['slip'], "No 'advice' key in 'slip'"

    print(f"Received advice: {data['slip']['advice']}")
