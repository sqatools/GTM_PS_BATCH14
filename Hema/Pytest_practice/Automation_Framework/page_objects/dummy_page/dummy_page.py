#from base.selenium_base import SeleniumBase
from base.selenium_base import SeleniumBase
from .dummy_page_locator import DummyPageLocator

class DummyPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
      #  self.driver = driver#???

    def launch_website(self, url):
        self.driver.get(url)

    def enter_first_name(self, value):
        self.enter_text(DummyPageLocator.FIRST_NAME, value)

    def enter_last_name(self, value):
        self.enter_text(DummyPageLocator.LAST_NAME, value)

    def get_title(self):
        return self.driver.title

    def enter_address(self, value):
        self.enter_text(DummyPageLocator.BILLING_ADDRESS, value)

    def enter_email_address(self, value):
        self.enter_text(DummyPageLocator.EMAIL_ADDRESS, value)

    # phase1 utilities
    def get_ticket_options(self):
        # returns list of radio button elements for tickets
        return self.driver.find_elements(*DummyPageLocator.TICKET_OPTIONS)

    def get_ticket_option_count(self):
        return len(self.get_ticket_options())

    def select_ticket_by_index(self, index):
        options = self.get_ticket_options()
        if index < len(options):
            options[index].click()
        else:
            raise IndexError(f"Ticket index {index} out of range")

    def is_ticket_selected(self, index):
        options = self.get_ticket_options()
        if index < len(options):
            return options[index].is_selected()
        raise IndexError(f"Ticket index {index} out of range")

    def is_element_present(self, locator):
        try:
            self.get_element(locator)
            return True
        except Exception:
            return False



    