from ...base.selenium_base import SeleniumBase
from .page_locators import Page_locator
class Login_page(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def launch_site(self, url):
        return self.driver.get(url)
    
    def enter_first_name(self, value):
        self.enter_text(Page_locator.F_name, value)

    def enter_last_name(self, value):
        self.enter_text(Page_locator.L_Name, value)

    def enter_address(self, value):
        self.enter_text(Page_locator.Address, value)