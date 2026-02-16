#create generic methods here which can be used in all the test cases
from selenium.webdriver.support.wait import WebDriverWait   
from selenium.webdriver.support import expected_conditions as ec  
from selenium.webdriver.support.select import Select


class SeleniumBase: 
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        elem =self.wait.until(ec.presence_of_element_located(locator))
        return elem
    
    def click(self, locator):
        elem = self.get_element(locator)
        elem.click()

    def enter_text(self, locator, text):
        elem = self.get_element(locator)
        elem.send_keys(text)

    def get_element(self, locator):
        elem = self.wait.until(ec.presence_of_element_located(locator))
        return elem
    
    def get_element_text(self, locator):
        elem = self.get_element(locator)
        return elem.text
    
    def select_dropdown(self, locator, value):
        elem = self.get_element(locator)
        select = Select(elem)
        select.select_by_visible_text(value)

    def element_is_displayed(self, locator):
        elem = self.get_element(locator)
        return elem.is_displayed()
    