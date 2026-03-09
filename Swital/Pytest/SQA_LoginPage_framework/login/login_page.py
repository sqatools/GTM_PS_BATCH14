from ..base.base_driver import BasePage
from .login_locator import LoginLocators
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):

    def open_login_page(self):
        self.open("https://practice.expandtesting.com/login")

    def enter_username(self, username):
        self.enter_text(LoginLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(LoginLocators.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(LoginLocators.LOGIN_BUTTON)

    def login(self, username, password):

        self.enter_username(username)
        self.enter_password(password)
        self.click(LoginLocators.LOGIN_BUTTON)
        # wait until secure page loads
        self.wait.until(lambda driver: "secure" in driver.current_url)

    def login_with_enter(self, username, password):
        self.enter_username(username)
        element = self.find(LoginLocators.PASSWORD_INPUT)
        element.send_keys(password + Keys.ENTER)
    
    def is_login_successful(self):

        message = self.get_text(LoginLocators.SUCCESS_MESSAGE)
        return "secure area" in message.lower()

    def logout(self):

        # wait until logout button visible
        self.wait.until(lambda d: "secure" in d.current_url)
        self.click(LoginLocators.LOGOUT_BUTTON)
        # wait until login page appears again
        self.wait.until(lambda d: "login" in d.current_url)

    def clear_username(self):
        element = self.find(LoginLocators.USERNAME_INPUT)
        element.clear()

    def clear_password(self):
        element = self.find(LoginLocators.PASSWORD_INPUT)
        element.clear()

    def refresh_page(self):
        self.driver.refresh()

    def is_logout_visible(self):
        return self.is_visible(LoginLocators.LOGOUT_BUTTON)

    def get_success_message(self):
        return self.get_text(LoginLocators.SUCCESS_MESSAGE)
    
    def get_error_message(self):

        self.wait.until(lambda d: self.is_visible(LoginLocators.ERROR_MESSAGE))
        return self.get_text(LoginLocators.ERROR_MESSAGE)

    def login_expect_failure(self, username, password):

        self.enter_username(username)
        self.enter_password(password)
        self.click(LoginLocators.LOGIN_BUTTON)
    
    def open_secure_page(self):
        self.open("https://practice.expandtesting.com/secure")