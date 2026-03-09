from ...base.selenium_base import SeleniumBase 
from .dummy_page_locator import DummyPageLocator

class DummyPage(SeleniumBase):
    def __init__(self, driver):
        # Call the constructor of the parent class to initialize
        super().__init__(driver)  
        self.driver = driver

    def launch_website(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title
    
    def enter_first_name(self, value):
        self.enter_text(DummyPageLocator.FIRST_NAME, value)

    def enter_last_name(self, value):
        self.enter_text(DummyPageLocator.LAST_NAME, value)

    # helper that returns True if locator is found and displayed
    def is_element_visible(self, locator):
        element = self.get_element(locator)
        return element is not None and element.is_displayed()

    def enter_email(self, value):
        self.enter_text(DummyPageLocator.EMAIL, value)

    def enter_phone(self, value):
        self.enter_text(DummyPageLocator.PHONE, value)

    # value getters for assertions in phase2
    def get_first_name_value(self):
        return self.get_attribute(DummyPageLocator.FIRST_NAME, "value")

    def get_last_name_value(self):
        return self.get_attribute(DummyPageLocator.LAST_NAME, "value")

    def get_email_value(self):
        return self.get_attribute(DummyPageLocator.EMAIL, "value")

    def get_phone_value(self):
        return self.get_attribute(DummyPageLocator.PHONE, "value")

    # --------------------------------------
    # Phase 3 helpers
    def enter_departure_date(self, date_str):
        # date_str in yyyy-mm-dd
        self.enter_text(DummyPageLocator.DEPART_DATE, date_str)

    def enter_return_date(self, date_str):
        self.enter_text(DummyPageLocator.RETURN_DATE, date_str)

    def get_departure_date_value(self):
        return self.get_attribute(DummyPageLocator.DEPART_DATE, "value")

    def get_return_date_value(self):
        return self.get_attribute(DummyPageLocator.RETURN_DATE, "value")

    def select_passengers(self, value):
        # value corresponds to option value attribute
        select_element = self.get_element(DummyPageLocator.PASSENGER_SELECT)
        # use Select utility imported earlier
        from selenium.webdriver.support.ui import Select
        Select(select_element).select_by_value(value)

    def get_selected_passenger_value(self):
        select_element = self.get_element(DummyPageLocator.PASSENGER_SELECT)
        from selenium.webdriver.support.ui import Select
        sel = Select(select_element)
        return sel.first_selected_option.get_attribute('value')

    # ----------------
    # Phase 4 helpers
    def enter_visa_date(self, date_str):
        self.enter_text(DummyPageLocator.VISA_DATE, date_str)

    def get_visa_date_value(self):
        return self.get_attribute(DummyPageLocator.VISA_DATE, "value")

    def select_delivery_option(self, option):
        # option should be 'email', 'whatsapp', or 'both'
        if option.lower() == 'email':
            locator = DummyPageLocator.DELIVERY_EMAIL
        elif option.lower() == 'whatsapp':
            locator = DummyPageLocator.DELIVERY_WHATSAPP
        elif option.lower() == 'both':
            locator = DummyPageLocator.DELIVERY_BOTH
        else:
            raise ValueError(f"unknown delivery option {option}")
        self.click_element(locator)

    def get_selected_delivery(self):
        # return string identifier of selected radio
        if self.is_element_selected(DummyPageLocator.DELIVERY_EMAIL):
            return 'email'
        if self.is_element_selected(DummyPageLocator.DELIVERY_WHATSAPP):
            return 'whatsapp'
        if self.is_element_selected(DummyPageLocator.DELIVERY_BOTH):
            return 'both'
        return None

    # Phase 5 helpers
    def is_header_visible(self):
        # check page heading text to simulate confirmation presence
        try:
            h = self.driver.find_element_by_xpath("//h1[contains(text(),'Dummy Ticket Booking Website')]")
            return h.is_displayed()
        except Exception:
            return False