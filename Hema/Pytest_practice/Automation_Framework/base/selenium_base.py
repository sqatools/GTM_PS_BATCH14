import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.log = logging.getLogger(__name__)

    def get_element(self, locator):
        self.log.info(f"getting element with locator : {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))
        

    def click_element(self, locator):
        self.log.info(f"clicking on element : {locator}")
        element = self.get_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.get_element(locator)
        element.clear()
        self.log.info(f"entering text in the element: {locator}")
        element.send_keys(text)

    def get_text(self, locator):
        element = self.get_element(locator)
        return element.text


