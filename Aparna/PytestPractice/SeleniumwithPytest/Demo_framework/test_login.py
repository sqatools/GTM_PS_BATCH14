from re import M

import pytest
from page_locators import LoginPageLocators
from selenium_base import SeleniumBase

@pytest.mark.usefixtures("get_driver")
class TestLogin:
            
    
    @pytest.fixture(autouse=True)
    def setup(self):
        #whenever we use the class we should crete the object
        #why we use self --means In a class we need to create
        # varaible inside a class we use self
        #creating objects of pagelocators and seleniumbase to access variables
        self.lp=LoginPageLocators()
        self.sb=SeleniumBase(self.driver)
        
    def test_valid_login(self):
        self.sb.enter_text(self.lp.username, "user1@gmail.com")
        self.sb.enter_text(self.lp.password, "User@1234")
        self.sb.click_element(self.lp.login_button)
        
       