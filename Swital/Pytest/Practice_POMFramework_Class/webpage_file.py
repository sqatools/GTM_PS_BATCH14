from selenium_basefile import Selenium_base
from locators import Locator

class WebPage(Selenium_base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def launch_website(self, url):
        return self.driver.get(url)
    
    def enter_first_name(self, value):
        self.enter_text(Locator.F_name, value)

    def enter_last_name(self, value):
        self.enter_text(Locator.L_name, value)
