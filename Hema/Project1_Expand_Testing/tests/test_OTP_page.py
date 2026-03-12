from page_objects.OTP_page.OTP_page import OTPPage
from page_objects.OTP_page.OTP_page_data import *
import pytest
import time


@pytest.mark.usefixtures("get_driver")
class TestOTPPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.test_otp = OTPPage(self.driver)

    def test_otp_page(self):
        self.test_otp.launch_website(website_url)
        self.test_otp.enter_email(email_id)
        self.test_otp.click_send_otp()
        time.sleep(5)
        otp_message = self.test_otp.get_otp_message()
        assert "We've sent an OTP code to your email:" in otp_message