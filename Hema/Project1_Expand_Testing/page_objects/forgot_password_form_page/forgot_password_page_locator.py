from selenium.webdriver.common.by import By

class ForgotPasswordPageLocator:
    input_email_locator = (By.NAME, "email")
    retrieve_password_locator = (By.XPATH, "//button[text()='Retrieve password']")