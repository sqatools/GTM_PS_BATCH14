from base.selenium_base import SeleniumBase
from page_objects.login_page.login_page_locator import LoginPageLocator

class LoginPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_website(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.enter_text(LoginPageLocator.input_username_locator, username)

    def enter_password(self, password):
        self.enter_text(LoginPageLocator.input_password_locator, password)

    def click_login(self):
        self.click_element(LoginPageLocator.click_login_locator)