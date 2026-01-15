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
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# initialize the Chrome driver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")
# Using different locators to find elements
# GET By ID
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("Hema")

# GET By NAME
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("Hema123")
address_textarea = driver.find_element(By.NAME, "address")
address_textarea.clear()
address_textarea.send_keys("Sargam, Pune  Maharashtra India")

# GET By XPATH
radio_button = driver.find_element(By.XPATH, "//input[@value='female']")
radio_button.click()
time.sleep(10)

# GET By LINK_TEXT
link_element = driver.find_element(By.LINK_TEXT, "Python Basic Programs")
link_element.click()
time.sleep(5)

# GET By PARTIAL_LINK_TEXT
partial_link_element = driver.find_element(By.PARTIAL_LINK_TEXT, "Python If-Else")
partial_link_element.click()
time.sleep(5)
driver.close()
