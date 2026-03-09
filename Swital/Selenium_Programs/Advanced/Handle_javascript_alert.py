from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://sqatools.in/automation-practice-page/")

# First simple javascript popup with ok button
def simple_alert():

    simple_alert = driver.find_element(By.XPATH, "//button[text() = 'Simple Alert']")
    simple_alert.click()
    time.sleep(2)
    driver.switch_to.alert.dismiss()
    time.sleep(2)

# simple_alert()

# Second with two button ok and cancel
def Confirm_alert():
    confirm_alert = driver.find_element(By.XPATH, "//button[text() = 'Confirm Alert']")
    confirm_alert.click()
    time.sleep(2)
    alert_obj = driver.switch_to.alert
    #alert_obj.accept()
    alert_obj.dismiss()
    time.sleep(2)

# Confirm_alert()

# Third with text and two button after entering text
def Prompt_alert():
    prompt_alert = driver.find_element(By.XPATH, "//button[text() = 'Prompt Alert']")
    prompt_alert.click()
    time.sleep(2)
    alert_obj = driver.switch_to.alert
    print("Text:", alert_obj.text)
    alert_obj.send_keys("None")
    print("Text:", alert_obj.text)    
    time.sleep(2)
    alert_obj.accept()
    #alert_obj.dismiss()
    time.sleep(2)
    
Prompt_alert()