from selenium.webdriver.common.by import By

class OTPPageLocator:
    email_input_locator = (By.NAME, "email")    
    send_otp_button_locator = (By.XPATH, "//button[contains(text(),'Send OTP')]")
    otp_message_locator = (By.ID, "otp-message") 
    otp_input_locator = (By.NAME, "otp")
    verify_otp_button_locator = (By.ID, "btn-send-verify")