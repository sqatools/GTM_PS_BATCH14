from selenium.webdriver.common.by import By

class Page_locator:
    FIRST_NAME =(By.XPATH, "//span[contains(text(),'First Name')]/following-sibling::input")
    LAST_NAME = (By.XPATH, "//span[contains(text(),'11Last Name')]/following-sibling::input")