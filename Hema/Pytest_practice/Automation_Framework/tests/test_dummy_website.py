import pytest
import time
from page_objects.dummy_page.dummy_page import DummyPage
from page_objects.dummy_page.dummy_page_data import *


@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:

    @pytest.fixture(scope="function", autouse= True)
    def setup(self):
        self.test1 = DummyPage(self.driver)

    def test_provide_user_details(self):
        self.test1.launch_website(url= website_URL)
        print(self.test1.get_title())
        self.test1.enter_first_name(first_name_value)
        self.test1.enter_last_name(last_name_value)
        self.test1.enter_address(address_value)
        self.test1.enter_email_address(email_value)

        time.sleep(5)