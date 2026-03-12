from selenium.webdriver.common.by import By

class DragAndDropPageLocator:
    source_element_locator = (By.ID, "column-a")
    target_element_locator = (By.ID, "column-b")