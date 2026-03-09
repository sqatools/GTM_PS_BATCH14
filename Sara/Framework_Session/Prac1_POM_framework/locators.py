from selenium.webdriver.common.by import By

class SqaPageLocator:
    FIRST_NAME = (By.XPATH, "//span[contains(text(),'First Name')]/following-sibling::input")
    LAST_NAME = (By.XPATH, "//span[contains(text(),'Last Name')]/following-sibling::input")