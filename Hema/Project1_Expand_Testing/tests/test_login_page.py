from page_objects.login_page.login_page_data import website_url, input_username, input_password
from page_objects.login_page.login_page import LoginPage
import pytest
import time


@pytest.mark.usefixtures("get_driver")
class TestLoginPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.test_login = LoginPage(self.driver)

    def test_login_page(self):
        self.test_login.launch_website(website_url)
        self.test_login.enter_username(input_username)
        self.test_login.enter_password(input_password)
        time.sleep(5)
        self.test_login.click_login()
        time.sleep(5)