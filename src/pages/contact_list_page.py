import time

from selenium.webdriver.common.alert import Alert

from resources.run_config import *
from src.common.common_web_element_func import CommonFunctions
from src.utils.locators import *


class ContactList:

    def __init__(self, driver):
        self.driver = driver

    def click_add_contact(self):
        ele = CommonFunctions.waitTillWebElementIsPresent(self.driver, ContactLocators.add_contact_btn)
        if ele is None:
            return False
        ele.click()

    def enter_contact_name(self,firstname,lastname):
        first_name = CommonFunctions.waitTillWebElementIsPresent(self.driver, ContactLocators.first_name)
        last_name = CommonFunctions.waitTillWebElementIsPresent(self.driver, ContactLocators.last_name)
        first_name.send_keys(firstname)
        last_name.send_keys(lastname)

    def click_submit(self):
        submit = CommonFunctions.waitTillWebElementIsPresent(self.driver, ContactLocators.submit_contact)
        submit.click()

    def create_new_contact(self,firstname,lastname):
        self.click_add_contact()
        self.enter_contact_name(firstname,lastname)
        self.click_submit()

    def get_contact_names(self):
        rows = CommonFunctions.getWebElements(self.driver,ContactLocators.contact_table_row)
        no_of_rows = len(rows)
        contact_list = []
        for i in range(1,no_of_rows):
            loc = (ContactLocators.contact_name_from_list[0] ,ContactLocators.contact_name_from_list[1].replace('i',str(i)))
            contact_name = CommonFunctions.waitTillWebElementIsPresent(self.driver, loc).text
            contact_list.append(contact_name)
        return contact_list

    def delete_contact(self,contact_name):
        loc = (ContactLocators.contact_name_field[0],ContactLocators.contact_name_field[1].replace('name',contact_name))
        print(CommonFunctions.waitTillWebElementIsPresent(self.driver, loc).text)
        CommonFunctions.waitTillWebElementIsPresent(self.driver, loc).click()
        time.sleep(1)
        CommonFunctions.waitTillWebElementIsPresent(self.driver, ContactLocators.delete_contact_btn).click()
        time.sleep(1)
        Alert(self.driver).accept()

    def verify_contact_deleted(self,contact_name):
        loc = (ContactLocators.contact_name_field[0], ContactLocators.contact_name_field[1].replace('name', contact_name))
        deleted_contact = CommonFunctions.waitTillWebElementIsPresent(self.driver, loc)
        if deleted_contact is None:
            return True




