from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Selenium_base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
    
    def get_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def get_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(text)    

    def get_text(self, locator):
        element = self.get_element(locator)
        return element.text
    
    def select_by_index(self, locator, index):
        element = self.get_element(locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        element = self.get_element(locator)
        Select(element).select_by_value(value)   

    def select_by_visible_text(self, locator, text):
        element = self.get_element(locator)
        Select(element).select_by_visible_text(text)   

    def multicheckbox_selection(self, locator):
        elements = self.get_elements(locator)
       # time.sleep(2)
        for element in elements:
            if not element.is_selected():
                element.click()