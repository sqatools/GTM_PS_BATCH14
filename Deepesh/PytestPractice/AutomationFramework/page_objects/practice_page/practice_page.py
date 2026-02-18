from ...base.selenium_base import SeleniumBase
from .practice_page_locators import PracticePageLocators

class PracticePage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_url(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.enter_text(PracticePageLocators.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.enter_text(PracticePageLocators.PASSWORD_FIELD, password)

    def enter_address(self, address):
        self.enter_text(PracticePageLocators.ADDRESS_FIELD, address)

    def enter_login_details(self, username, password, address):
        self.enter_username(username)
        self.enter_password(password)
        self.enter_address(address)

    
    def get_radion_button_status(self, gender):
        if gender.lower() == "male":
            return self.is_element_selected(PracticePageLocators.MALE_RADIO_BUTTON)
        elif gender.lower() == "female":
            return self.is_element_selected(PracticePageLocators.FEMALE_RADIO_BUTTON)


    def select_radio_button(self, gender):
        if gender.lower() == "male":
            self.click_element(PracticePageLocators.MALE_RADIO_BUTTON)
        elif gender.lower() == "female":
            self.click_element(PracticePageLocators.FEMALE_RADIO_BUTTON)


    
    def select_checkbox(self, checkbox_name):
        if checkbox_name.lower() == "java":
            self.click_element(PracticePageLocators.JAVA_CHECKBOX)
        elif checkbox_name.lower() == "python":
            self.click_element(PracticePageLocators.PYTHON_CHECKBOX)
        elif checkbox_name.lower() == "selenium":
            self.click_element(PracticePageLocators.SELENIUM_CHECKBOX)

    def get_checkbox_status(self, checkbox_name):
        if checkbox_name.lower() == "java":
            return self.is_element_selected(PracticePageLocators.JAVA_CHECKBOX)
        elif checkbox_name.lower() == "python":
            return self.is_element_selected(PracticePageLocators.PYTHON_CHECKBOX)
        elif checkbox_name.lower() == "selenium":
            return self.is_element_selected(PracticePageLocators.SELENIUM_CHECKBOX)
        

    def select_country(self, country_name):
        self.select_dropdown_option(PracticePageLocators.COUNTRY_DROPDOWN, country_name)


    def upload_file_on_web(self, file_path):
        self.upload_file(PracticePageLocators.UPLOAD_FILE_INPUT, file_path)


