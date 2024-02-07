import json
import requests
from resources.run_config import *
from src.utils.api_data import *


class UserAPI:

    def get_user_data(self, token):
        try:
            user_headers = {"Authorization": "Bearer " + token}
            user_headers.update(content_type)
            user_data_url = url + user_data_endpoint
            user_resp = requests.get(user_data_url, headers=user_headers)
            return user_resp.json()["email"]
        except:
            return user_resp.status_code
