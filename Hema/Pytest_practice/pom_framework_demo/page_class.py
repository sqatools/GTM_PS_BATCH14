from seleniumbase import Selenium_Base
from page_locator import Page_Locator

class page_class(Selenium_Base):
    def __init__(self, driver):
         # Call the constructor of the parent class to initialize
        super().__init__(driver)
        self.driver = driver

    def launch_website(self, URL):
        self.driver.get(URL)
      
    def get_title(self):
        return self.driver.title
    
    def enter_first_name(self, value):
        self.enter_text(Page_Locator.First_Name, value)

    def enter_last_name(self, value):
        self.enter_text(Page_Locator.Last_Name, value)
