import pytest
import time
from ...Page_objects.Dummy_Page.dummy_page import DummyPage
from ...Page_objects.Dummy_Page.dummy_page_data import *

@pytest.mark.usefixtures("get_driver")

class TestDummyWebsite:

    @pytest.fixture(scope='function', autouse=True)

    def setup(self):
        self.dp=DummyPage(self.driver)

    def test_provide_user_details(self):
        self.dp.launch_website(url=website_url)
        self.dp.enter_first_name(first_name_value)
        self.dp.enter_last_name(last_name_value)
        time.sleep(5)


