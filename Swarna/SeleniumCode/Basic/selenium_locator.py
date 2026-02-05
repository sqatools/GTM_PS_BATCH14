import time
from selenium import webdriver
from selenium.webdriver.common.by import By



"""
Selenium Locators:
    ID :# covered 
    XPATH 
    LINK_TEXT# covered
    PARTIAL_LINK_TEXT #  covered
    NAME #: covered
    TAG_NAME #  covered
    CLASS_NAME 
    CSS_SELECTOR 

"""

# initialize the Chrome driver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")

# Using different locators to find elements
# GET By TAG_NAME
heading_element = driver.find_element(By.TAG_NAME, "h1")
print("Heading Text:", heading_element.text)


# Name locator
name_input = driver.find_element(By.NAME, "username")
name_input.send_keys("testuser")
time.sleep(2)

password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("password123")
time.sleep(2)

text_area_Address = driver.find_element(By.NAME, "address")
text_area_Address.send_keys("123, Test Street, Test City")
time.sleep(2)

radio_button = driver.find_element(By.ID, "female")
radio_button.click()
time.sleep(2)   

# ID locator
java_checkbox = driver.find_element(By.ID, "java")
java_checkbox.click()
time.sleep(2)

calendar_input = driver.find_element(By.ID, "datePicker")
calendar_input.send_keys("12/31/2024")

time_field = driver.find_element(By.ID, "timePicker")
time_field.send_keys("10:30 AM")

date_time_field = driver.find_element(By.ID, "dateTimePicker")
date_time_field.send_keys("12/31/2024 10:30 AM")


# LINK_TEXT locator
google_link = driver.find_element(By.LINK_TEXT, "Open Google")
google_link.click()
time.sleep(5)

# PARTIAL_LINK_TEXT locator
partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Bottom")
partial_link.click()
time.sleep(5)


# XPATH locator # press key element
press_keys = driver.find_element(By.XPATH, "//input[@placeholder='Press any key']")
press_keys.click()
time.sleep(5)
