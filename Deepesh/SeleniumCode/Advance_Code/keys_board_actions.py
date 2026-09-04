from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/automation-practice-page/")
def perform_keyboard_actions():
    input_field = driver.find_element(By.ID, "username")
    time.sleep(5)
    # use tab key to focus on the input field
    input_field.send_keys(Keys.TAB)
    time.sleep(5)
  

    
    # type text in uppercase using SHIFT key
    text_area  = driver.find_element(By.ID, "address")
    text_area.send_keys(Keys.SHIFT, "We are Learning Python Programming")
    time.sleep(5)
    # select all text using CONTROL + A
    text_area.send_keys(Keys.CONTROL, 'a')
    time.sleep(5)
    # copy the selected text using CONTROL + C
    text_area.send_keys(Keys.CONTROL, 'c')
    time.sleep(5)

    input_field.send_keys(Keys.CONTROL, 'v')  # paste the copied text using CONTROL + V
    time.sleep(5)

    radio_elem  = driver.find_element(By.ID, "male")
    print(radio_elem.is_selected())
    radio_elem.send_keys(Keys.SPACE)  # select the radio button using SPACE key
    time.sleep(5)




perform_keyboard_actions()