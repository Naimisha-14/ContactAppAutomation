from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonFunctions():

    @staticmethod
    def waitTillWebElementIsClickable(driver,locator):
        try:
            return WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
        except:
            return

    @staticmethod
    def waitTillWebElementIsPresent(driver,locator):
        try:
            return WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
        except:
            return

    @staticmethod
    def getWebElements(driver, locator):
        try:
            return WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located(locator))
        except:
            return