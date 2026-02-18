import pytest
import time
from data_file import *
from page_class import page_class

@pytest.mark.usefixtures("get_driver")
class Test_Website:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.test1 = page_class(self.driver)

    def test1_enterdetails(self):
        self.test1.launch_website(URL = Website_URL)
        self.test1.enter_first_name(first_name_value)
        self.test1.enter_last_name(last_name_value)
        
        time.sleep(10)


