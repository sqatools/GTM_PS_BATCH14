from selenium.webdriver.common.by import By

class Page_Locator:
    First_Name = (By.XPATH, "//span[contains(text(),'First Name')]/following-sibling::input")
    Last_Name = (By.XPATH, "//span[contains(text(),'Last Name')]/following-sibling::input")