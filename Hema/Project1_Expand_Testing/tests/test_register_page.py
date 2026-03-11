from page_objects.register_page.register_page_data import *
from page_objects.register_page.register_page_locator import RegisterPageLocator
from page_objects.register_page.register_page import RegisterPage
import pytest
import time


@pytest.mark.usefixtures("get_driver")
class TestRegisterPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.test_register = RegisterPage(self.driver)

    def test_register_page(self):
        self.test_register.launch_website(website_url)
        self.test_register.enter_username(input_username)
        self.test_register.enter_password(input_password)
        self.test_register.confirm_password(confirm_password)
        time.sleep(5)
        self.test_register.click_register()

        time.sleep(5)