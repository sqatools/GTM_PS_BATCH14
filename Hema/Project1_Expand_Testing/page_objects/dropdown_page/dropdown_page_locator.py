from selenium.webdriver.common.by import By

class DropdownPageLocator:
    dropdown_locator = (By.ID, "dropdown")
    #option1_locator = (By.XPATH, "//option[text()='Option 1']")
    #option2_locator = (By.XPATH, "//option[text()='Option 2']")
    elements_per_page_locator = (By.ID, "elementsPerPageSelect")
    country_locator = (By.ID, "country")