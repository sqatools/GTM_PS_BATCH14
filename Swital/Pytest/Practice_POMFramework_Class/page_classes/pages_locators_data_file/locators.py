from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class Locator:
    F_name = (By.XPATH, "//span[contains(text(), 'First Name')]/following-sibling::input[@name = 'firstname']")
    L_name = (By.XPATH, "//span[contains(text(), 'Last Name')]/following-sibling::input[@name = 'firstname']")
    radio_gender = (By.ID, "female")
    no_passenger = (By.ID, "admorepass")
    