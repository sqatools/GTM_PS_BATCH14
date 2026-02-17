from selenium.webdriver.common.by import By
class Locator:
    F_name = (By.XPATH, "(//input[@name='firstname'])[1]")
    L_name = (By.XPATH, "(//input[@name='firstname'])[2]")