import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.maximize_window
driver.implicitly_wait(20)

driver.get("https://sqatools.in/automation-practice-page/")

def handle_simple_alert():
    alert_btn = driver.find_element(By.XPATH, "//button[text()='Simple Alert']")
    alert_btn.click()
    time.sleep(5)
    alert_obj = Alert(driver)
    print(alert_obj.text)
    alert_obj.accept()
    time.sleep(2)

#handle_simple_alert()

def handle_confirm_alert():
    alert_btn = driver.find_element(By.XPATH, "//button[text()='Confirm Alert']")
    alert_btn.click()
    time.sleep(5)
    alert_obj = Alert(driver)
    print(alert_obj.text)

    #alert_obj.accept() # it will click on OK button
    alert_obj.dismiss # It will click on Cancel button


handle_confirm_alert()

