import random

import pytest

from src.pages.contact_list_page import ContactList
from src.pages.login_page import Login


@pytest.fixture(scope='class')
def sign_in(login_fixture):
    login_page = Login(login_fixture)
    return login_page

@pytest.fixture(scope='class')
def launch_browser(open_browser):
    browser = Login(open_browser)
    return browser

@pytest.fixture(scope='class')
def contact_page(login_fixture):
    contact_obj = ContactList(login_fixture)
    return contact_obj


@pytest.mark.usefixtures('launch_browser')
class TestLogin:

    @pytest.mark.parametrize('email,password,error_msg',[('abc','abc','Incorrect username or password'),('abc@abc.co.com','password','Incorrect username or password')])
    def test_login(self, launch_browser,email,password,error_msg):
        assert launch_browser.verify_login(email,password) == error_msg

    def test_login_valid(self, sign_in):
        assert sign_in.verify_user_logged_in() is True, "User did not login"

@pytest.mark.usefixtures('contact_page')
class TestContactPage:
    def test_add_contact(self,contact_page):
        global first_name, last_name
        first_name = 'First '+str(random.randrange(12,1234))
        last_name = 'Last ' + str(random.randrange(12, 1234))
        contact_page.create_new_contact(first_name,last_name)

    def test_verify_contact_created(self,contact_page):
        contact_names = contact_page.get_contact_names()
        print(contact_names)
        assert first_name + ' ' + last_name in contact_names, "User is not added"

    def test_delete_created_contact(self,contact_page):
        contact_page.delete_contact(first_name + ' ' + last_name)
        deleted_flag = contact_page.verify_contact_deleted(first_name + ' ' + last_name)
        assert deleted_flag is True, 'Contact is deleted'



