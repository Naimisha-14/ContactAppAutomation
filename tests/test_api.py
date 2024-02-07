import pytest

from resources.run_config import *
from src.api_func.login_api_func import LoginAPI
from src.api_func.user_api_func import UserAPI


@pytest.fixture(scope='class')
def login_object():
    login_obj = LoginAPI()
    return login_obj

@pytest.fixture(scope='class')
def user_obj():
    user_object = UserAPI()
    return user_object


@pytest.mark.usefixtures('login_api')
class TestLoginAPI:

    def test_login_valid(self,login_api):
        assert login_api is not None, 'Login is not successful'

    @pytest.mark.parametrize('email,passwd,status',[('abc','pass',401)])
    def test_invalid_login(self, login_object,email,passwd,status):
        actual_status_code = login_object.login_invalid(email,passwd)
        assert actual_status_code == status, f"Expected status code is {status} but actual response status code is {actual_status_code}"

@pytest.mark.usefixtures('login_api')
class TestUserData:

    def test_get_logged_in_user_data(self,login_api,user_obj):
        token = login_api
        email_id = user_obj.get_user_data(token)
        assert email_id == email_address, "User data is invalid"

    @pytest.mark.parametrize('token,status',[("invalid_token",401)])
    def test_get_logged_in_user_data_invalid(self,login_api,user_obj,token,status):
        actual_status = user_obj.get_user_data(token)
        assert actual_status == status, f"Expected status is {status} but actual status is {actual_status}"

