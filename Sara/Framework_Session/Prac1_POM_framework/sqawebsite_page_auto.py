from selenium_base import SeleniumBase 
from locators import SqaPageLocator

class SqaPage(SeleniumBase):
    def __init__(self, driver):
        # Call the constructor of the parent class to initialize
        super().__init__(driver)  
        self.driver = driver

    def launch_website(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title
    
    def enter_first_name(self, value):
        self.enter_text(SqaPageLocator.FIRST_NAME, value)

    def enter_last_name(self, value):
        self.enter_text(SqaPageLocator.LAST_NAME, value)