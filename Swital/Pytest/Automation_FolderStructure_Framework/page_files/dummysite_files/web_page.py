from ...base.selenium_base import SeleniumBase
from .pagewise_locators import Page_locator

class WebPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def launch_website(self, url):
        self.driver.get(url)
    
    def get_title(self):
        return self.driver.title
    
    def enter_first_name(self, value):
        self.enter_text(Page_locator.FIRST_NAME, value)

    def enter_last_name(self, value):
        self.enter_text(Page_locator.LAST_NAME, value)  
    