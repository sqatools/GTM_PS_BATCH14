from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class SeleniumBase():
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,20)

    def get_element(self,locator):
        return self.wait.until(ec.presence_of_element_located(locator))
    
    def click_element(self,locator):
        element=self.get_element(locator)
        element.click()

    def enter_text(self,locator,text):
        element=self.get_element(locator)
        element.clear()
        element.send_keys(text)
