from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

#selenium actions

class SeleniumBase:
    #constructor required a parameter
    #when we create aobject the parameter of constructor is provide
    def __init__(self, driver):
        self.driver = driver
        # Initialize explicit WebDriverWait with a timeout of 20 seconds
        self.wait = WebDriverWait(self.driver, 20)

    def get_element(self, locator):
        elem = self.wait.until(ec.presence_of_element_located(locator))
        return elem
    
    def click_element(self, locator):
        elem = self.get_element(locator)
        elem.click()

    def enter_text(self, locator, value):
        elem = self.get_element(locator)
        elem.clear()
        elem.send_keys(value)

    def get_elements(self, locator):
        elems = self.wait.until(ec.presence_of_all_elements_located(locator))
        return elems
    
    def get_element_text(self, locator):
        elem = self.get_element(locator)
        return elem.text
    

    def select_dropdown(self, locator, value): 
        elem = self.get_element(locator)
        select = Select(elem)
        select.select_by_visible_text(value)


    
    


    
