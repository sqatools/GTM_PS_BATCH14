import pytest
import time
from web_page import WebPage
from page_testdata import *

@pytest.mark.usefixtures("get_driver")
class TestWebsite:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.wp = WebPage(self.driver)
    def test_provide_user_details(self):
        self.wp.launch_website(website)
        self.wp.enter_first_name(first_name)
        self.wp.enter_last_name(last_name)