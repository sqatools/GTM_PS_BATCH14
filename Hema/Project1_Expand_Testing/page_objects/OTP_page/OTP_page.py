from base.selenium_base import SeleniumBase
from page_objects.OTP_page.OTP_page_locator import OTPPageLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    
    def enter_otp(self, otp, timeout=20):
        otp_field = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(OTPPageLocator.otp_input_locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", otp_field)
        otp_field.clear()
        otp_field.send_keys(otp)

    def click_verify_otp(self):
        self.click_element(OTPPageLocator.verify_otp_button_locator)