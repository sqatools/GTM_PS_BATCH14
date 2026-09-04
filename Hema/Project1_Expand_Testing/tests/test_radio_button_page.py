from page_objects.radio_button_page.radio_button_page_locator import RadioButtonPageLocator
from page_objects.radio_button_page.radio_button_page_data import *
from page_objects.radio_button_page.radio_button_page import RadioButtonPage
import pytest
import time

@pytest.mark.usefixtures("get_driver")
class TestRadioButtonPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.test_radio_button = RadioButtonPage(self.driver)

    def test_radio_button_page(self):
        self.test_radio_button.launch_website(website_url)
        time.sleep(5)
        self.test_radio_button.click_radio_button_1()
        self.test_radio_button.click_radio_button_2()
        #self.test_radio_button.click_radio_button_3()
        #self.test_radio_button.click_radio_button_4()
        #self.test_radio_button.click_radio_button_5()
        #self.test_radio_button.click_basketball_button()
        time.sleep(5)
        self.test_radio_button.click_football_button()
        #self.test_radio_button.click_tennis_button()
        
        time.sleep(5)