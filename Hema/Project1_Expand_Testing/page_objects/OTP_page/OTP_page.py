from base.selenium_base import SeleniumBase
from page_objects.OTP_page.OTP_page_locator import OTPPageLocator

class OTPPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_website(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        self.enter_text(OTPPageLocator.email_input_locator, email)

    def click_send_otp(self):
        self.click_element(OTPPageLocator.send_otp_button_locator)

    def get_otp_message(self):
        return self.get_text(OTPPageLocator.otp_message_locator)