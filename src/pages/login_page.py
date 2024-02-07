import time
from resources.run_config import *
from src.common.common_web_element_func import CommonFunctions
from src.utils.locators import *


class Login:

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        ele = CommonFunctions.waitTillWebElementIsPresent(self.driver, LoginLocators.email_txt_bx)
        ele.clear()
        ele.send_keys(email)
        if ele is None:
            return False

    def enter_password(self, password):
        ele = CommonFunctions.waitTillWebElementIsPresent(self.driver, LoginLocators.passwd_tx_bx)
        ele.clear()
        ele.send_keys(password)
        if ele is None:
            return False

    def clickOnSignIn(self):
        ele = CommonFunctions.waitTillWebElementIsPresent(self.driver, LoginLocators.login_btn)
        if ele is None: return False
        ele.click()

    def login_valid(self):
        self.enter_email(email_address)
        self.enter_password(passwd)
        self.clickOnSignIn()

    def verify_user_logged_in(self):
        logout_button = CommonFunctions.waitTillWebElementIsPresent(self.driver,LoginLocators.logout_btn)
        print(logout_button)
        if logout_button is None:
            return False
        return True

    def login_error_msg(self):
        error_msg = CommonFunctions.waitTillWebElementIsPresent(self.driver,LoginLocators.login_err)
        print(error_msg.text)
        return error_msg.text

    def verify_login(self,email,password):
        self.enter_email(email)
        self.enter_password(password)
        self.clickOnSignIn()
        time.sleep(1)
        return self.login_error_msg()


