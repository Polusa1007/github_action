import os
import configparser
import requests

class LoginSetUp:
    def __init__(self, config=None, request_post=None):
        self.config = config if config else self._get_config()
        self.request_post = request_post if request_post else requests.post
        self.base_url = self._get_base_url()

    def _get_config(self):
        dir_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(dir_path, 'credential.ini')
        config = configparser.ConfigParser()
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file '{config_path}' not found.")
        config.read(config_path)
        return config

    def _get_base_url(self):
        if 'section_a' not in self.config:
            raise configparser.NoSectionError('section_a')
        return self.config.get('section_a', 'url')

    def login(self):
        api_url = f'{self.base_url}/account_login'
        headers = {
            'Content-Type': 'application/json'
        }
        account_data = {
            'account': self.config.get('section_a', 'account'),
            'password': self.config.get('section_a', 'password'),
        }
        response = self.request_post(api_url, headers=headers, json=account_data)
        print(response)
        if response.status_code != 200:
            raise Exception(f"Login failed with status code {response.status_code}")
        token = response.json().get('access_token', '')
        if not token:
            raise Exception("No access token received.")
        return token
