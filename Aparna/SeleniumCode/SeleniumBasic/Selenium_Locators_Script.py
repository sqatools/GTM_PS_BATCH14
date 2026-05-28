"""
Selenium Locators:
    ID: ByType = "id"
    XPATH: ByType = "xpath"
    LINK_TEXT: ByType = "link text"
    PARTIAL_LINK_TEXT: ByType = "partial link text"
    NAME: ByType = "name"
    TAG_NAME: ByType = "tag name"
    CLASS_NAME: ByType = "class name"
    CSS_SELECTOR: ByType = "css selector"
    cd.\basic\selenium_locators_script.py
    
    https://sqatools.in/automation-practice-page/
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By



#initialize the Chrome driver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")

#Locator by TAG_NAME
heading_element=driver.find_element(By.TAG_NAME, "h1")
print("Heading Text:", heading_element.text)

#Locator by name
name_input=driver.find_element(By.NAME, "username")
name_input.send_keys("testuser")

password_input=driver.find_element(By.NAME, "password")
password_input.send_keys("password123")

text_area_Address=driver.find_element(By.NAME, "address")
text_area_Address.send_keys("123, Test Street, Test City Johnusbhurg")
time.sleep(5)


#Locator by ID
radio_btn=driver.find_element(By.ID, "female")
radio_btn.click()
time.sleep(2)

python_checkbox=driver.find_element(By.ID, "python")
python_checkbox.click()
time.sleep(5)

date_picker=driver.find_element(By.ID, "datePicker")
date_picker.send_keys("05/28/2026")
time.sleep(5)

time_picker=driver.find_element(By.ID, "timePicker")
time_picker.send_keys("15:30 AM")
time.sleep(5)

date_time_picker=driver.find_element(By.ID, "dateTimePicker")
date_time_picker.send_keys("05/28/2026 15:30 AM")
time.sleep(5)

#Locator by LINK_TEXT
google_link=driver.find_element(By.LINK_TEXT, "Open Google")
google_link.click()
time.sleep(3)


#Locator by PARTIAL_LINK_TEXT
partial_link=driver.find_element(By.PARTIAL_LINK_TEXT, "Bottom")
partial_link.click()
time.sleep(3)
