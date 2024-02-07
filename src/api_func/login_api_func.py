import json
import requests
from resources.run_config import *
from src.utils.api_data import *


class LoginAPI:

    def login(self):
        try:
            login_body = {"email": email_address, "password": passwd}
            login_url = url + login_endpoint
            login_response = requests.post(login_url, data=json.dumps(login_body), headers=content_type)
            return (login_response.json()["token"])
        except:
            return None

    def login_invalid(self,email,password):

        login_body = {"email": email, "password": password}
        login_url = url + login_endpoint
        login_response = requests.post(login_url, data=json.dumps(login_body), headers=content_type)
        return login_response.status_code
