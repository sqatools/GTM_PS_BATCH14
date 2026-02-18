import pytest
import time
import os
from ...page_objects.practice_page.practice_page import PracticePage
from ...page_objects.practice_page.practice_page_data import *

@pytest.mark.usefixtures("get_driver")
class TestPracticePage:
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.pp = PracticePage(self.driver)


    def test_enter_user_details_verify(self):
        self.pp.launch_url(url=practice_url)
        self.pp.enter_login_details(username=username_value,
                                    password=password_value,
                                    address=address_value)
        self.pp.select_radio_button(gender=radio_selection)
        assert self.pp.get_radion_button_status(gender=radio_selection)
        self.pp.select_checkbox(checkbox_name=checkbox_selection)
        assert self.pp.get_checkbox_status(checkbox_name=checkbox_selection)
        self.pp.select_country(country_name=country_name)
        with open("data_file.txt", "w") as file:
            file.write("We are learning framework")
        file_path_upload = os.path.join(os.getcwd(), "data_file.txt")
        self.pp.upload_file_on_web(file_path=file_path_upload)

        time.sleep(10)


