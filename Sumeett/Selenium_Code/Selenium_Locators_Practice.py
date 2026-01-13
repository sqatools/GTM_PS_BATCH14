
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

""""
Selenium Locators:
    ID : covered 
    XPATH 
    LINK_TEXT : covered
    PARTIAL_LINK_TEXT  : covered
    NAME  : covered
    TAG_NAME 
    CLASS_NAME 
    CSS_SELECTOR 

"""
# initialize the Chrome driver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")

#Use different locators for practice
#ID
Enter_Username = driver.find_element(By.ID, "username")
Enter_Username.send_keys("testuser")
time.sleep(2)

Enter_Password = driver.find_element(By.ID, "password")
Enter_Password.send_keys("password123")
time.sleep(2)

#Name locator
Enter_address = driver.find_element(By.NAME, "address")
Enter_address.send_keys("XYZ society, MG Road, Mumbai")
time.sleep(5)

Select_Gender = driver.find_element(By.ID, "male")
Select_Gender.click()
time.sleep(5)

Select_Checkbox = driver.find_element(By.ID, "python")
Select_Checkbox.click()
time.sleep(5)

Select_Dropdown = driver.find_element(By.NAME, "country")
Select_Dropdown.send_keys("India")
time.sleep(5)

#Select_Multi_Dropdown = driver.find_element(By.id, "skills")
#Select_Multi_Dropdown.send_keys("Python")
#time.sleep(5)


Select_Button = driver.find_element(By.ID, "normalButton")
Select_Button.click()
time.sleep(5)   

Select_DatePicker = driver.find_element(By.ID, "datePicker")
Select_DatePicker.send_keys("01/13/2026")
time.sleep(5)

Select_time = driver.find_element(By.ID, "timePicker")
Select_time.send_keys("10:44 PM")
time.sleep(5)

Select_datetimepicker = driver.find_element(By.ID, "dateTimePicker")
Select_datetimepicker.send_keys("01/13/2026 10:44 PM")
time.sleep(5)


#Partial link text locators
Select_Partial_Link = driver.find_element(By.PARTIAL_LINK_TEXT, "Bottom")
Select_Partial_Link.click()
time.sleep(10)

#Link text locators

Select_Links = driver.find_element(By.LINK_TEXT, "Open Google")
Select_Links.click()
time.sleep(5)

