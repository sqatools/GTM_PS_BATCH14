import pytest
from page_locators import LoginPageLocators
from selenium_base import SeleniumBase

@pytest.mark.usefixtures("get_driver")
class TestLogin:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.lp = LoginPageLocators()
        self.sb = SeleniumBase(self.driver)

    def test_valid_login(self):
        self.sb.enter_text(self.lp.USERNAME, "user1@gmail.com")
        self.sb.enter_text(self.lp.PASSWORD, "User@1234")
        self.sb.click_element(self.lp.LOGIN_BUTTON)


    def test_invalid_login(self):
        self.sb.enter_text(self.lp.USERNAME, "invalid_user@gmail.com")
        self.sb.enter_text(self.lp.PASSWORD, "Invalid@1234")
        self.sb.click_element(self.lp.LOGIN_BUTTON)
        
