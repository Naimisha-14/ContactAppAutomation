from selenium.webdriver.common.by import By


class LoginLocators:
    email_txt_bx = (By.ID,'email')
    passwd_tx_bx = (By.ID,'password')
    login_btn = (By.ID,'submit')
    logout_btn = (By.ID,'logout')
    login_err = (By.XPATH,'//span[@id="error"]')

class ContactLocators:
    add_contact_btn = (By.ID,'add-contact')
    first_name = (By.ID,'firstName')
    last_name = (By.ID,'lastName')
    submit_contact = (By.ID,'submit')
    contact_table_row = (By.XPATH,'//tr[@class="contactTableBodyRow"]')
    contact_name_from_list = (By.XPATH,'//tr[i]//td[2]')
    contact_name_field = (By.XPATH,'//td[normalize-space()="name"]')
    delete_contact_btn = (By.ID,'delete')
