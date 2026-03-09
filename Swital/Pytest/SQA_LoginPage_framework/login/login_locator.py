from selenium.webdriver.common.by import By

class LoginLocators:

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")

    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    ERROR_MESSAGE = (By.ID, "flash")

    SUCCESS_MESSAGE = (By.ID, "flash")

    LOGOUT_BUTTON = (By.XPATH, "//a[contains(@href,'logout')]")