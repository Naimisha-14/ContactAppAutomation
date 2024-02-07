import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from resources.run_config import *
from src.api_func.login_api_func import LoginAPI
from src.pages.login_page import Login
@pytest.fixture(scope='class')
def open_browser():
    global driver
    service_obj = Service(executable_path='drivers/chromedriver.exe')
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    driver.set_window_size(1920, 1080)
    driver.get(url)
    yield driver  # Provides webdriver instance to tests
    driver.quit() # Teardown: closes the browsers

@pytest.fixture(scope='class')
def login_fixture(open_browser):
    login_obj = Login(driver)
    login_obj.login_valid()
    yield driver

@pytest.fixture(scope='class')
def login_api(scope='class'):
    login_obj = LoginAPI()
    token = login_obj.login()
    return token




