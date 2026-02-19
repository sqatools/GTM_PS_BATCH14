from selenium.webdriver.common.by import By

class DummyPageLocator:
   FIRST_NAME = (By.XPATH, "//span[contains(text(), 'First Name')]/following-sibling::input")
   LAST_NAME = (By.XPATH, "//span[contains(text(), 'Last Name')]/following-sibling::input")
   BILLING_ADDRESS = (By.ID, "billing_address")
   EMAIL_ADDRESS = (By.ID, "billing_email")