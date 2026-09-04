from base.selenium_base import SeleniumBase
from page_objects.register_page.register_page_locator import RegisterPageLocator

class RegisterPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_website(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.enter_text(RegisterPageLocator.input_username_locator, username)

    def enter_password(self, password):
        self.enter_text(RegisterPageLocator.input_password_locator, password)

    def confirm_password(self, confirm_password):
        self.enter_text(RegisterPageLocator.confirm_password_locator, confirm_password)

    def click_register(self):
        self.click_element(RegisterPageLocator.click_register_locator)