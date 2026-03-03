import pytest
import time
from ...page_objects.dummy_page.dummy_page import DummyPage
from ...page_objects.dummy_page.dummy_page_data import *
from ...page_objects.dummy_page.dummy_page_locator import DummyPageLocator

# call the fixture to initialize the WebDriver and provide it to the test class
@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.dp = DummyPage(self.driver)

    @pytest.mark.ui
    def test_open_site_and_verify_title(self):
        # Phase 1 - TC1
        self.dp.launch_website(url=website_url)
        title = self.dp.get_title()
        assert "Dummy Booking" in title, f"unexpected title: {title}"

    @pytest.mark.ui
    def test_verify_essential_elements(self):
        # Phase 1 - TC2
        self.dp.launch_website(url=website_url)
        assert self.dp.is_element_visible(DummyPageLocator.FIRST_NAME)
        assert self.dp.is_element_visible(DummyPageLocator.LAST_NAME)
        assert self.dp.is_element_visible(DummyPageLocator.EMAIL)
        assert self.dp.is_element_visible(DummyPageLocator.PHONE)

    @pytest.mark.ui
    def test_provide_user_details(self):
        # existing test (will eventually be part of phase2)
        self.dp.launch_website(url=website_url)
        self.dp.enter_first_name(first_name_value)
        self.dp.enter_last_name(last_name_value)
        time.sleep(5)

    @pytest.mark.ui
    def test_enter_personal_names(self):
        # Phase 2 - TC3
        self.dp.launch_website(url=website_url)
        self.dp.enter_first_name(first_name_value)
        self.dp.enter_last_name(last_name_value)
        assert self.dp.get_first_name_value() == first_name_value
        assert self.dp.get_last_name_value() == last_name_value

    @pytest.mark.ui
    def test_enter_contact_info(self):
        # Phase 2 - TC4
        self.dp.launch_website(url=website_url)
        self.dp.enter_email(email_value)
        self.dp.enter_phone(phone_value)
        assert self.dp.get_email_value() == email_value
        assert self.dp.get_phone_value() == phone_value

    @pytest.mark.ui
    def test_select_booking_dates(self):
        # Phase 3 - TC5
        self.dp.launch_website(url=website_url)
        self.dp.enter_departure_date(departure_date_value)
        self.dp.enter_return_date(return_date_value)
        # value formatting can vary; just ensure field is populated
        dep_val = self.dp.get_departure_date_value()
        ret_val = self.dp.get_return_date_value()
        assert dep_val and '-' in dep_val, f"unexpected depart date value: {dep_val}"
        assert ret_val and '-' in ret_val, f"unexpected return date value: {ret_val}"

    @pytest.mark.ui
    def test_choose_passengers(self):
        # Phase 3 - TC6 (room type/quantity interpreted as passenger count)
        self.dp.launch_website(url=website_url)
        self.dp.select_passengers(passenger_option_value)
        assert self.dp.get_selected_passenger_value() == passenger_option_value

    @pytest.mark.ui
    def test_fill_optional_fields(self):
        # Phase 4 - TC7
        self.dp.launch_website(url=website_url)
        self.dp.enter_visa_date(visa_date_value)
        # select delivery option and assert
        self.dp.select_delivery_option(delivery_option)
        # date control may re-format value; just verify something was set
        vis_val = self.dp.get_visa_date_value()
        assert vis_val and '-' in vis_val, f"unexpected visa date value: {vis_val}"
        assert self.dp.get_selected_delivery() == delivery_option
        # no actual submit button exists; ensure page title still valid
        assert "Dummy Booking" in self.dp.get_title()

    @pytest.mark.ui
    def test_reset_form_after_navigation(self):
        # Phase 5 - TC10 (navigate back to home and check blank)
        self.dp.launch_website(url=website_url)
        # fill a value
        self.dp.enter_first_name(first_name_value)
        # re-launch to simulate returning home
        self.dp.launch_website(url=website_url)
        # field should be empty
        assert self.dp.get_first_name_value() in ("", None)

    @pytest.mark.ui
    def test_confirmation_placeholder(self):
        # Phase 5 - TC9 (no real confirmation, simple title check)
        self.dp.launch_website(url=website_url)
        title = self.dp.get_title()
        assert "Dummy Booking" in title, f"unexpected title after pseudo-submit: {title}"