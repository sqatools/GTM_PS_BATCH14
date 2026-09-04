from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")

def handle_alert():
    #get heading tittle
    heading=driver.find_element(By.XPATH,"//section//h2[text()='JavaScript Alerts']")
    time.sleep(5)
    heading.click()
    print("heading:",heading.text)
    
    #simple alert
    simple_alert_button=driver.find_element(By.XPATH,"//section//button[text()='Simple Alert']")
    simple_alert_button.click()
    time.sleep(5)
    #create object for alert class
    alert_obj=Alert(driver)
    print("Alert messgae:", alert_obj.text)
    alert_obj.accept()
    time.sleep(2)
#handle_alert()

def handle_ConfirmAlert():
    Alert_heading=driver.find_element(By.XPATH,"//button[@onclick='showConfirm()']")
    Alert_heading.click()
    time.sleep(4)
    alert_obj=Alert(driver)
    print("Alert message:", alert_obj.text)
    alert_obj.accept()# to click ok
    alert_obj.dismiss()#cancel alert
    time.sleep(5)
#handle_ConfirmAlert()

def handle_PromptAlert():
    alert_obj=Alert(driver)
    driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")

    prompt_button=driver.find_element(By.XPATH,"//button[@id='promptbtn']")
    prompt_button.click()
    time.sleep(5)
    
    
   
    print("Alert message:", alert_obj.text)
    alert_obj.send_keys("Aparna QA")
    alert_obj.accept()
    time.sleep(5)
    #print the messgae after accept
    message=driver.find_element(By.ID,"prompt")
    print(message.text)
handle_PromptAlert()

    
    
    