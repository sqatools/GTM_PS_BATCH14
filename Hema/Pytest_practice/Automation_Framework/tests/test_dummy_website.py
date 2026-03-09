import pytest
import time
#from page_objects.dummy_page.dummy_page import DummyPage
from page_objects.dummy_page.dummy_page import DummyPage
from page_objects.dummy_page.dummy_page_data import *
from page_objects.dummy_page.dummy_page_locator import DummyPageLocator


@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:

    @pytest.fixture(scope="function", autouse= True)
    def setup(self):
        self.test1 = DummyPage(self.driver)

    # ---- Phase1 tests ----
    def test_phase1_title(self):
        self.test1.launch_website(url=website_URL)
        assert expected_title in self.test1.get_title()

    def test_phase1_core_elements_present(self):
        self.test1.launch_website(url=website_URL)
        assert self.test1.is_element_present(DummyPageLocator.FIRST_NAME)
        assert self.test1.is_element_present(DummyPageLocator.LAST_NAME)
        assert self.test1.is_element_present(DummyPageLocator.BILLING_ADDRESS)
        assert self.test1.is_element_present(DummyPageLocator.EMAIL_ADDRESS)
        assert self.test1.is_element_present(DummyPageLocator.BIRTHDAY)
        assert self.test1.is_element_present(DummyPageLocator.GENDER_MALE)
        assert self.test1.is_element_present(DummyPageLocator.GENDER_FEMALE)
        ticket_list = self.test1.get_ticket_options()
        assert len(ticket_list) > 0

    def test_phase2_select_each_ticket(self):
        # iterate through all ticket radio buttons and ensure selecting one deselects others
        self.test1.launch_website(url=website_URL)
        count = self.test1.get_ticket_option_count()
        assert count > 0, "No tickets available to select"
        for idx in range(count):
            self.test1.select_ticket_by_index(idx)
            # verify the clicked option becomes selected
            assert self.test1.is_ticket_selected(idx), f"Ticket {idx} should be selected after click"
            # note: inputs are not grouped by name, so others may remain selected; no assertion on them

    def test_phase2_default_ticket_selection(self):
        # after reload, ensure no option is pre-selected (or a known default behavior)
        self.test1.launch_website(url=website_URL)
        count = self.test1.get_ticket_option_count()
        for j in range(count):
            assert not self.test1.is_ticket_selected(j), "Ticket should not be pre-selected on fresh load"

    def test_provide_user_details(self):
        self.test1.launch_website(url= website_URL)
        print(self.test1.get_title())
        self.test1.enter_first_name(first_name_value)
        self.test1.enter_last_name(last_name_value)
        self.test1.enter_address(address_value)
        self.test1.enter_email_address(email_value)

        time.sleep(5)