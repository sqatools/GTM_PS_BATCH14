import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Selenium interacct with webbrowser(Firefoox,Edge,chrome etc) through driver so we make obhject of driver

"""
# driver= webdriver.Edge()
# driver.get("https://sqatools.in/dummy-booking-website/") # open website
# driver.implicitly_wait(10)
# driver.maximize_window()
# # Here ID is called locator or selector to find elements on website
# first_name_field=driver.find_element(By.ID,"firstname") # We right click on First Name text box and click on inspect and see id of element(textbox)
# first_name_field.send_keys("SATISH") # Sendkey method used to enter value in textbox(Input tag wale textbox hote hai
# #last_name_field=driver.find_element(By.ID,"")
# date_of_birth_field=driver.find_element(By.ID,"birthday")
# date_of_birth_field.send_keys("10-02-2026")
#
# male_radio_button=driver.find_element(By.ID,"male")
# male_radio_button.click()
# time.sleep(5)

# Secondwebsite practise
#https://sqatools.in/automation-practice-page/

# driver=webdriver.Edge()
# driver.get("https://sqatools.in/automation-practice-page/")
# driver.implicitly_wait(10)
# driver.maximize_window()
# open_google_link=driver.find_element(By.LINK_TEXT,"Open Google")
# open_google_link.click()
#
# python_check_box=driver.find_element(By.ID,"python")
# python_check_box.click()
# time.sleep(10)

############# RELATIVE xpath locator or selector to select element on webpage #####################
#https://sqatools.in/dummy-booking-website/
# In above url First Name and Last Name textbox have same name and id so we select then with xpath as follows:
#In Selenium with Python, a relative XPath using indexing is used when multiple elements match the same XPath and you want to select a specific one by position.
#1️⃣ Basic syntax of indexed relative XPath
#(xpath_expression)[index]
#✔ Index starts from 1, not 0. Note
# driver=webdriver.Edge()
# driver.get("https://sqatools.in/dummy-booking-website/")
# driver.implicitly_wait(10)
# driver.maximize_window()
# first_name_element=driver.find_element(By.XPATH,"(//input[@name='firstname'])[1]")
# first_name_element.send_keys('Jyoti')
# last_name_element=driver.find_element(By.XPATH,"(//input[@name='firstname'])[2]")
# last_name_element.send_keys('Paliwal')
#
# time.sleep(5)

##### use of text() method to write relative xpath and find element on webpage

# driver=webdriver.Edge()
# driver.get("https://sqatools.in/automation-practice-page/")
# driver.implicitly_wait(10)
# driver.maximize_window()
# confirm_alert_button_element=driver.find_element(By.XPATH,"//button[text()='Confirm Alert']")
#
# time.sleep(5)

##### use of contains() method to write relative xpath and find element on webpage
# driver=webdriver.Edge()
# driver.get("https://sqatools.in/automation-practice-page/")
# driver.implicitly_wait(10)
# driver.maximize_window()
# Automation_Practice_Page=driver.find_element(By.XPATH,"//h1[contains(text(),'Automation')]")
#OR
#Automation_Practice_Page=driver.find_element(By.XPATH,"//h1[contains(@class,'entry')]") # attribute class has value entry-title but we have given partial value as per syntax

# time.sleep(5)

#####Practise of Orange HRM website https://opensource-demo.orangehrmlive.com/web/index.php/auth/login######################

driver=webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)
driver.maximize_window()
user_name_field=driver.find_element(By.NAME,'username')
user_name_field.send_keys('Admin')

user_name_field=driver.find_element(By.NAME,'password')
user_name_field.send_keys('admin123')

login_button_field=driver.find_element(By.XPATH,"//button[@type='submit']")
login_button_field.click()
time.sleep(5)