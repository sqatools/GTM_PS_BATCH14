import pytest
from ...page_classes.pages_locators_data_file.webpage_file import WebPage
from ...page_classes.pages_locators_data_file.test_datafile import *
import time

@pytest.mark.usefixtures("get_driver")
class TestFile:
    @pytest.fixture(scope="function", autouse=True)

    def setup(self):
        self.wp = WebPage(self.driver)

    def test_credential_flow(self):
        self.wp.launch_website(website_url)
        self.wp.enter_first_name(first_name)
        self.wp.enter_last_name(last_name)
        self.wp.click_on_gender()
        self.wp.select_passenger(2)
        self.wp.cities_multicheckbox()
        time.sleep(5)