from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/automation-practice-page/")

def execute_javascript():
    # remove disabled attribute from the textbox
    disable_element = driver.find_element(By.ID, "disabledInput")
    driver.execute_script("arguments[0].removeAttribute('disabled')", disable_element)
    time.sleep(5)
    disable_element.send_keys("Entering text into enabled textbox")
    time.sleep(10)

    # enable hidden element and enter text
    hidden_element = driver.find_element(By.ID, "hiddenField")
    driver.execute_script("arguments[0].style.display='block';", hidden_element)
    hidden_element.send_keys("Entering text into now visible textbox")
    time.sleep(10)

    
    
execute_javascript()