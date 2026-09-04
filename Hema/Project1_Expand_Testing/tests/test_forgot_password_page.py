from page_objects.forgot_password_form_page.forgot_password_page_locator import ForgotPasswordPageLocator
from page_objects.forgot_password_form_page.forgot_password_page import ForgotPasswordPage
from page_objects.forgot_password_form_page.forgot_password_page_data import *
import pytest
import time


@pytest.mark.usefixtures("get_driver")
class TestForgotPasswordPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.test_forgot_password = ForgotPasswordPage(self.driver)

    def test_forgot_password_page(self):
        self.test_forgot_password.launch_website(website_url)
        self.test_forgot_password.enter_email(enter_email)
        time.sleep(5)
        self.test_forgot_password.click_retrieve_password()

        time.sleep(5)