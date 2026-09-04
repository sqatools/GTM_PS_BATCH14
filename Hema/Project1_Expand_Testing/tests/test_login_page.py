from page_objects.login_page.login_page_data import *
from page_objects.login_page.login_page import LoginPage
import pytest
import time


@pytest.mark.usefixtures("get_driver")
#Indicates that this test class will use a fixture named get_driver.
#Usually, get_driver is defined elsewhere to initialize a Selenium WebDriver (like Chrome or Firefox).
#This allows self.driver to be available in the tests.
class TestLoginPage:

    @pytest.fixture(scope="function", autouse=True)
#In pytest, a fixture is a way to set up preconditions before running a test and optionally clean up after the test.
#scope="function" means the fixture will run once for each test function.
# autouse=-true will automatically run this fixture for every test function in the class without needing to explicitly call it.
    def setup(self):
        self.test_login = LoginPage(self.driver)

    def test_login_page(self):
        self.test_login.launch_website(website_url)
        self.test_login.enter_username(input_username)
        self.test_login.enter_password(input_password)
        time.sleep(5)
        self.test_login.click_login()
        time.sleep(5)

    def test_login_with_incorrect_credentials(self):# because of autouse no need to pass setup as parameter
        self.test_login.launch_website(website_url)
        self.test_login.enter_username(incorrect_username)
        self.test_login.enter_password(incorrect_password)
        time.sleep(5)
        self.test_login.click_login()
        time.sleep(5)