#habdle alerts in selenium- javascript popups
import selenium
from selenium import webdriver  
import time 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")
#click on simple alert button
def handle_simple_alerts():
    alert_button = driver.find_element(By.XPATH, "//button[text()='Simple Alert']")
    alert_button.click()
    time.sleep(5)
    alert_obj = Alert(driver) #important to write this line to handle alert
    print(alert_obj.text)
    alert_obj.accept()
    time.sleep(2)
handle_simple_alerts()

#click on confirm alert button
def handle_confirm_alert():
    alert_button = driver.find_element(By.XPATH, "//button[text()='Confirm Alert']")
    alert_button.click()
    time.sleep(5)
    alert_obj = Alert(driver) #important to write this line to handle alert
    print(alert_obj.text)
    alert_obj.dismiss() #it will click on cancel button
    time.sleep(2)
handle_confirm_alert()

#click on prompt alert button
def prompt_alert():
    alert_button = driver.find_element(By.XPATH, "//button[text()='Prompt Alert']")
    alert_button.click()
    time.sleep(5)
    alert_obj = Alert(driver) #important to write this line to handle alert
    print(alert_obj.text)
    alert_obj.send_keys("Selenium")
    alert_obj.accept()
    time.sleep(2)
    
prompt_alert()

time.sleep(5)
driver.quit()
