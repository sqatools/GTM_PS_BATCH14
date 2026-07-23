from ...base.selenium_base import SeleniumBase
from .practice_page_locators import PracticePageLocators


class PracticePage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def launch_url(self, url):
        self.driver.get(url)

    def launchurl(self, url):
        self.launch_url(url)

    def enter_username(self, value):
        self.logger.info(f"Entering username: {value}")
        self.enter_text(PracticePageLocators.USERNAME, value)

    def enter_password(self, value):
        self.logger.info(f"Entering password: {value}")
        self.enter_text(PracticePageLocators.PASSWORD, value)

    def enter_address(self, value):
        self.logger.info(f"Entering address: {value}")
        self.enter_text(PracticePageLocators.ADDRESS, value)

    def enter_login_details(self, username, password, address):
        self.enter_username(username)
        self.enter_password(password)
        self.enter_address(address)

    def get_radio_button_status(self, gender):
        self.logger.info(f"Checking radio button status for gender: {gender}")
        if gender.lower() == "male":
            return self.is_element_selected(PracticePageLocators.MALE_RADIOBUTTON)
        elif gender.lower() == "female":
            return self.is_element_selected(PracticePageLocators.FEMALE_RADIOBUTTON)

    def get_radion_button_status(self, gender):
        return self.get_radio_button_status(gender)

    def select_radio_button(self, gender):
        self.logger.info(f"Selecting radio button for gender: {gender}")
        if gender.lower() == "male":
            self.click_element(PracticePageLocators.MALE_RADIOBUTTON)
        elif gender.lower() == "female":
            self.click_element(PracticePageLocators.FEMALE_RADIOBUTTON)

    def select_checkbox(self, checkbox_name):
        self.logger.info(f"Selecting checkbox: {checkbox_name}")
        if checkbox_name.lower() == "java":
            self.click_element(PracticePageLocators.JAVA_CHECKBOX)
        elif checkbox_name.lower() == "python":
            self.click_element(PracticePageLocators.PYTHON_CHECKBOX)
        elif checkbox_name.lower() == "selenium":
            self.click_element(PracticePageLocators.SELENIUM_CHECKBOX)

    def get_checkbox_status(self, checkbox_name):
        self.logger.info(f"Checking checkbox status for: {checkbox_name}")
        if checkbox_name.lower() == "java":
            return self.is_element_selected(PracticePageLocators.JAVA_CHECKBOX)
        elif checkbox_name.lower() == "python":
            return self.is_element_selected(PracticePageLocators.PYTHON_CHECKBOX)
        elif checkbox_name.lower() == "selenium":
            return self.is_element_selected(PracticePageLocators.SELENIUM_CHECKBOX)

    def select_country(self, country_name):
        self.logger.info(f"Selecting country: {country_name}")
        self.select_dropdown(PracticePageLocators.COUNTRY_DROPDOWN, country_name)

    def upload_file(self, file_path):
        self.logger.info(f"Uploading file: {file_path}")
        super().upload_file(PracticePageLocators.UPLOAD_FILE, file_path)

    def upload_file_on_web(self, file_path):
        self.upload_file(file_path)