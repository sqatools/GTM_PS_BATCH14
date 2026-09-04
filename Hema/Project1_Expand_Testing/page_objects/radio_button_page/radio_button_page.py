from base.selenium_base import SeleniumBase
from page_objects.radio_button_page.radio_button_page_locator import RadioButtonPageLocator

class RadioButtonPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_website(self, url):
        self.driver.get(url)

    def click_radio_button_1(self):
        self.click_element(RadioButtonPageLocator.radio_button_1_locator)

    def click_radio_button_2(self):
        self.click_element(RadioButtonPageLocator.radio_button_2_locator)

    def click_radio_button_3(self):
        self.click_element(RadioButtonPageLocator.radio_button_3_locator)

    def click_radio_button_4(self):
        self.click_element(RadioButtonPageLocator.radio_button_4_locator)

    def click_radio_button_5(self):
        self.click_element(RadioButtonPageLocator.radio_button_5_locator)

    def click_basketball_button(self):
        self.click_element(RadioButtonPageLocator.basketball_button_locator)

    def click_football_button(self):
        self.click_element(RadioButtonPageLocator.football_button_locator)

    def click_tennis_button(self):
        self.click_element(RadioButtonPageLocator.tennis_button_locator)