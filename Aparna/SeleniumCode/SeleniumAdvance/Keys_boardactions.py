#keyboard action ctrl A,Ctrl V C, sentkeys,enter text,move to the tabs
import time

from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/automation-practice-page/")

def keys_handle():

    input_username_field=driver.find_element(By.ID,"username")
    #USE TAB KEY FOCUS ON NEXT FIELD
    input_username_field.send_keys(Keys.TAB)
    time.sleep(5)
    #input_username_field.send_keys("Test")
    #time.sleep(5)
    
    # Type text in upper case by using SHIF key
    text_address=driver.find_element(By.ID, "address")
    text_address.send_keys(Keys.SHIFT,"Lering sleenium pyhton")
    time.sleep(5)
    
    #Using contolr+A to select text
    text_address.send_keys(Keys.CONTROL, 'a')
    time.sleep(5)
    
    #Using control+C to copy the selected text
    text_address.send_keys(Keys.CONTROL, 'c')
    
      
    #Using control+V to paste the slected text
    input_username_field.send_keys(Keys.CONTROL,'v')
    time.sleep(5)
    
     # select the radio button using SPACE key
    radio_elem  = driver.find_element(By.ID, "male")
    print(radio_elem.is_selected())
    radio_elem.send_keys(Keys.SPACE) 
    time.sleep(5)
    
keys_handle()
