from base.selenium_base import SeleniumBase
from .web_inputs_locator import WebInputsLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebInputsPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 20)

    def launch_website(self, url):
        self.driver.get(url)

    def hover_web_inputs_link(self):
        self.click_link(WebInputsLocator.link_web_inputs)

    def enter_number(self, value):
        self.wait.until(EC.element_to_be_clickable(WebInputsLocator.input_number_locator))
        self.enter_text(WebInputsLocator.input_number_locator, value)

    def enter_text_input(self, value):
        self.wait.until(EC.element_to_be_clickable(WebInputsLocator.input_text_locator))
        self.enter_text(WebInputsLocator.input_text_locator, value) 

    def enter_password(self, value):
        self.wait.until(EC.element_to_be_clickable(WebInputsLocator.input_password_locator))
        self.enter_text(WebInputsLocator.input_password_locator, value)

    def enter_date(self, value):
        self.wait.until(EC.element_to_be_clickable(WebInputsLocator.input_date_locator))
        self.enter_text(WebInputsLocator.input_date_locator, value) 

    