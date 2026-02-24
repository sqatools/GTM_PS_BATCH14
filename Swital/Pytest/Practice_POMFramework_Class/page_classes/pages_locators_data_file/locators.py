from selenium.webdriver.common.by import By

class Locator:
    F_name = (By.XPATH, "//span[contains(text(), 'First Name')]/following-sibling::input[@name = 'firstname']")
    L_name = (By.XPATH, "//span[contains(text(), 'Last Name')]/following-sibling::input[@name = 'firstname']")
    radio_gender = (By.ID, "female")
    no_passenger = (By.ID, "admorepass")
    multicity_checkboxes = (By.XPATH, "//th[text()='City Name']/parent::tr/following-sibling::tr//input")

    