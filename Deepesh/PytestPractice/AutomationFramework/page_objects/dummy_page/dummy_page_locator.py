from selenium.webdriver.common.by import By

class DummyPageLocator:
    FIRST_NAME = (By.XPATH, "//span[contains(text(),'First Name')]/following-sibling::input")
    LAST_NAME = (By.XPATH, "//span[contains(text(),'Last Name')]/following-sibling::input")
    # added in support for phase1 tests
    EMAIL = (By.ID, "billing_email")
    PHONE = (By.ID, "billing_phone")
    # other elements can be added later (dates, dropdowns, etc.)

    # Phase 3 locators
    DEPART_DATE = (By.ID, "departdate")
    RETURN_DATE = (By.ID, "returndate")
    PASSENGER_SELECT = (By.ID, "admorepass")

    # Phase 4 locators
    VISA_DATE = (By.ID, "visadate")
    DELIVERY_EMAIL = (By.ID, "eamil")
    DELIVERY_WHATSAPP = (By.ID, "whatsapp")
    DELIVERY_BOTH = (By.ID, "female")  # reused id for Both option

    # Phase 5 isn't about new locators but might reuse existing ones (first name etc.)