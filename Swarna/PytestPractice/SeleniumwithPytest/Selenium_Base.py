from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class SeleniumAction:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=30)


    def get_element(self, locator):
        #e.g self.wait.until(ec.presence_of_element_located((By.XPATH, "//a[text()='value']")))
        element = self.wait.until(ec.presence_of_element_located(locator))
        return element
    
    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def enter_text(self, locator, value):
        element = self.get_element(locator)
        element.clear()
        element.send_keys()



