import pytest
from ...page_classes.pages.login_page import Login_page
from ...page_classes.pages.test_data import Testdata_file

@pytest.mark.usefixtures("get_driver")
class Test_loginFun:
    @pytest.fixture(scope="function", autouse="True")
    
    def setup(self):
        self.tp = Login_page(self.driver)

    def test_login_functionality_positivecase(self):
        self.tp.launch_site(Testdata_file.Website)
        self.tp.enter_first_name(Testdata_file.First_name)
        self.tp.enter_last_name(Testdata_file.Last_name)
        self.tp.enter_address(Testdata_file.Address)