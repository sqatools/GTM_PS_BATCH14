import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")

name_input = driver.find_element(By.NAME, "username")
name_input.send_keys("testuser")
time.sleep(2)

password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("testpass")
time.sleep(2)

address_input = driver.find_element(By.NAME, "address")
address_input.send_keys("123, Test Street, Test City")
time.sleep(5)

# male_radio = driver.find_element(By.ID, "male")
# male_radio.click()
# time.sleep(2)

# female_radio = driver.find_element(By.ID, "female")
# female_radio.click()
# time.sleep(2)

# other_radio = driver.find_element(By.ID, "other")
# other_radio.click()
# time.sleep(2)

# java_checkbox = driver.find_element(By.ID, "java")
# java_checkbox.click()
# time.sleep(2)

# python_checkbox = driver.find_element(By.ID, "python")
# python_checkbox.click()
# time.sleep(2)

# selenium_checkbox = driver.find_element(By.ID, "selenium")
# selenium_checkbox.click()
# time.sleep(2)

# dropdown_element = driver.find_element(By.ID, "country")
# select = Select(dropdown_element)
# select.select_by_value("india")
# time.sleep(2)

# multi_select_element = driver.find_element(By.ID, "skills")
# multi_select = Select(multi_select_element)
# multi_select.select_by_visible_text("Python")
# #multi_select.select_by_value("Selenium") 
# multi_select.select_by_index(3)
# time.sleep(2)

# Normal_button = driver.find_element(By.ID, "normalButton")
# Normal_button.click()
# time.sleep(1)

# Submit_button = driver.find_element(By.ID, "submitButton")
# Submit_button.click()
# time.sleep(1)

# Reset_button = driver.find_element(By.ID, "resetButton")
# Reset_button.click()
# time.sleep(1)

# #Alert Handling
# #Simple pop-up alert
# driver.find_element(By.XPATH, "//button[text()='Simple Alert']").click()

# alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
# time.sleep(5)
# #print(alert.text)
# alert.accept()
# time.sleep(2)

#confirm pop-up alert
#driver.find_element(By.XPATH, "//button[text()='Confirm Alert']").click()
# alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
# time.sleep(5)
# alert.dismiss()   # OK
# time.sleep(2)

#Prompt pop-up alert
# driver.find_element(By.XPATH, "//button[text()='Prompt Alert']").click()
# alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
# time.sleep(5)
# alert.send_keys("Selenium Test")
# alert.accept()
# time.sleep(2)


#File Upload
# file_upload= driver.find_element(By.ID, "fileupload")
# file_upload.send_keys("D:\\PythonAutomation\\GTM_PS_BATCH14\\Achin\\firstfile.py")
# time.sleep(2)
# driver.quit()

#Calendar
# mm_dd_yyyy = driver.find_element(By.ID, "datePicker")
# mm_dd_yyyy.send_keys("12/31/2024")
# time.sleep(2)
# hh_mm_ss = driver.find_element(By.ID, "timePicker")
# hh_mm_ss.send_keys("10:30 AM")
# time.sleep(2)
# date_time = driver.find_element(By.ID, "dateTimePicker")
# date_time.send_keys("12/31/2024 10:30 AM")  
# time.sleep(2)

#Links
# bottom_link = driver.find_element(By.LINK_TEXT, "Go to Bottom")
# bottom_link.click()
# time.sleep(2)

#IFrame
# Use WebDriverWait to wait for element to be clickable
# learn_more_link = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[text()='Learn more']"))
# )
# learn_more_link.click()
# time.sleep(2)

#Enabled and Disabled Elements
input_box = driver.find_element(
    By.XPATH, "//input[@type='text' and @id='enabledInput']"
)

input_box.clear()
input_box.send_keys("New Text")
time.sleep(2)

disabled_input = driver.find_element(
    By.XPATH, "//input[@type='text' and @id='disabledInput']"
)

#print("Is input enabled before:", disabled_input.is_enabled())
#print("Current value:", disabled_input.get_attribute("value"))

driver.execute_script(
    "document.getElementById('disabledInput').removeAttribute('disabled');"
)
disabled_input.clear()
disabled_input.send_keys("Now I can type")
time.sleep(2)
driver.quit()   