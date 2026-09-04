from selenium_base import SeleniumBase 
from dummy_page_locator import DummyPageLocator

class DummyPage(SeleniumBase):
    def __init__(self, driver):
        # Call the constructor of the parent class to initialize
        super().__init__(driver)  
        self.driver = driver

    def launch_website(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title
    
    def enter_first_name(self, value):
        self.enter_text(DummyPageLocator.FIRST_NAME, value)

    def enter_last_name(self, value):
        self.enter_text(DummyPageLocator.LAST_NAME, value)