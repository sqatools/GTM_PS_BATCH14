import pytest
from login_page import Login_page
from test_data import *

@pytest.mark.usefixtures("get_driver")
class Test_loginFun:
    @pytest.fixture(scope="function", autouse="True")
    def setup(self):
        self.tp = Login_page(self.driver)
    def login_functionality_positivecase(self):
        self.tp.launch_site(Website)
        self.tp.enter_first_name(First_name)
        self.tp.enter_last_name(Last_name)
        self.tp.enter_address(Address)