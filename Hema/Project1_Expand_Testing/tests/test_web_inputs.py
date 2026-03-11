from page_objects.web_inputs_page.web_input_data import *
from page_objects.web_inputs_page.web_inputs_locator import WebInputsLocator
from page_objects.web_inputs_page.web_inputs_page import WebInputsPage
import pytest
import time

@pytest.mark.usefixtures("get_driver")
class TestWebInputs:

    @pytest.fixture(scope="function", autouse = True)
    def setup(self):
        self.test_web_inputs = WebInputsPage(self.driver)

    def test_web_inputs(self):
        self.test_web_inputs.launch_website(website_url)
        time.sleep(5)
        self.test_web_inputs.enter_number(input_number)
        self.test_web_inputs.enter_text_input(input_text)
        self.test_web_inputs.enter_password(input_password)
        self.test_web_inputs.enter_date(input_date)         

        time.sleep(5)
