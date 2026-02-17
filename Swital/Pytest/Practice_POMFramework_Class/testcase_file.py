import pytest
from webpage_file import WebPage
from test_datafile import *

@pytest.mark.usefixtures("get_driver")
class TestFile:
    @pytest.fixture(scope="function", autouse=True)

    def setup(self):
        self.wp = WebPage(self.driver)

    def test_credential_flow(self):
        self.wp.launch_website(website_url)
        self.wp.enter_first_name(first_name)
        self.wp.enter_last_name(last_name)

