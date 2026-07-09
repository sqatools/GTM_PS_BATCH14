

from  selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def get_element(self, locator):
        ele = self.wait.until(ec.presence_of_element_located(locator))
        return ele
        
        
    def clcik_element(self,locator):
        ele=self.get_element(locator)
        ele.click()
        
    def enter_text(self,locator,value):
        ele=self.get_element(locator)
        ele.clear()
        ele.send_keys(value)
        
    def get_text(self,locator):
        ele=self.get_element(locator)
        return ele.text
    
    def get_elements(self,locator):
        ele=self.wait.until(ec.presence_of_all_elements_located(locator))
        return ele
    
    def get_element_text(self,locator):
        ele=self.wait.until(ec.presence_of_element_located(locator))
        return ele.text
    
    
    #selct radio button method
    def select_radio_button(self,locator):
        ele=self.get_element(locator)
        if not ele.is_selected():
            ele.click()
            
    #select checkbox method
    def select_checkbox(self,locator):
        ele=self.get_element(locator)
        if not ele.is_selected():
            ele.click()
            
    #select dropdown method
    def select_dropdown(self,locator):
        ele=self.get_element(locator)
        ele.click()