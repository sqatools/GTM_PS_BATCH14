import pytest
import time
from sqawebsite_page_auto import SqaPage
from testdata import *

# call the fixture to initialize the WebDriver and provide it to the test class
@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.dp = SqaPage(self.driver)

    def test_provide_user_details(self):
        self.dp.launch_website(url=website_url)
        self.dp.enter_first_name(first_name_value)
        self.dp.enter_last_name(last_name_value)
        time.sleep(5)