from selenium.webdriver.common.by import By

class OTPPageLocator:
    email_input_locator = (By.NAME, "email")    
    send_otp_button_locator = (By.ID, "btn-send-otp")
    otp_message_locator = (By.ID, "otp-message") 