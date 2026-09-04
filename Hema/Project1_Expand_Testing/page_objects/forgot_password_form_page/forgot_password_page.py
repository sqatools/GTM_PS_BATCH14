from base.selenium_base import SeleniumBase
from page_objects.forgot_password_form_page.forgot_password_page_locator import ForgotPasswordPageLocator

class ForgotPasswordPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_website(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        self.enter_text(ForgotPasswordPageLocator.input_email_locator, email)

    def click_retrieve_password(self):
        self.click_element(ForgotPasswordPageLocator.retrieve_password_locator)     
   
    #def click_back_to_login(self):
      #  self.click_element(ForgotPasswordPageLocator.back_to_login_locator)
