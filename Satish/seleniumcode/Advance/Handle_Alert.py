import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver=webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/automation-practice-page/")
# In above website there are three Alert ubder Javascript alert menu

def handle_simple_alert():
    simple_alert_element=driver.find_element(By.XPATH,"//button[@onclick='showAlert()']")
    simple_alert_element.click()
    time.sleep(2)
    # To interact with Alert(pop-up comes when we click on simple alert button) menu we need Alert obj
    alert_obj=Alert(driver)
    print(alert_obj.text)
    time.sleep(5)
    alert_obj.accept() # It means clicking on OK button of Alert


#handle_simple_alert()

def handle_confirm_alert():
    simple_alert_element=driver.find_element(By.XPATH,"//button[@onclick='showConfirm()']")
    simple_alert_element.click()
    time.sleep(2)
    # To interact with Alert(pop-up comes when we click on simple alert button) menu we need Alert obj
    alert_obj=Alert(driver)
    print(alert_obj.text)
    time.sleep(5)
    alert_obj.accept() # It means clicking on OK button of Alert
    #alert_obj.dismiss() # It means clicking on Cancel button of Alert

#handle_confirm_alert()

def handle_prompt_alert():
    simple_alert_element=driver.find_element(By.XPATH,"//button[@onclick='showPrompt()']")
    simple_alert_element.click()
    time.sleep(2)
    # To interact with Alert(pop-up comes when we click on simple alert button) menu we need Alert obj
    alert_obj=Alert(driver)
    alert_obj.send_keys("Satish Paliwal")

    print(alert_obj.text)
    time.sleep(5)
    alert_obj.accept() # It means clicking on OK button of Alert
    #alert_obj.dismiss() # It means clicking on Cancel button of Alert

handle_prompt_alert()