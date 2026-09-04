'''
execute file with below command line
python .\AutomationPracPage.py
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")
driver.implicitly_wait(10)

title= driver.title
print("Page Title:", title)


page_heading=driver.find_element(By.CSS_SELECTOR, "h1[class='entry-title']")
print ("Page Heading", page_heading.text)

driver.find_element(By.NAME,"username").send_keys("Sara_D")
time.sleep(2)

driver.find_element(By.NAME,"password").send_keys("Sara01")
time.sleep(2)

driver.find_element(By.ID,"address").send_keys(" : Mumbai, India")
time.sleep(2)

driver.find_element(By.ID,"female").click()
time.sleep(2)

driver.find_element(By.ID,"java").click()
time.sleep(2)

driver.find_element(By.ID,"selenium").click()
time.sleep(2)

# Relative xpath- DropDown (Select) section
country_dropdown=driver.find_element(By.XPATH,"//select[@id='country']")
select_country= Select(country_dropdown)
select_country.select_by_value("india")
time.sleep(2)

# Relative xpath: text() method - Multi Select DropDown
driver.find_element(By.XPATH,"//option[text()='Python']").click()
time.sleep(2)

# Relative xpath: contains() method - Multi Select DropDown
driver.find_element(By.XPATH,"//option[contains(text(),'Play')]").click()
time.sleep(2)

# Relative xpath: starts-with() method - Button
driver.find_element(By.XPATH,"//button[starts-with(text(),'Normal')]").click()
time.sleep(2)

driver.find_element(By.XPATH,"//button[starts-with(@type,'res')]").click()
time.sleep(2)


driver.find_element(By.ID,"datePicker").send_keys("11/03/2026")
time.sleep(2)

driver.find_element(By.ID,"timePicker").send_keys("01:24 PM")
time.sleep(2)

driver.find_element(By.ID,"dateTimePicker").send_keys("12/03/2026 04:23 PM")
time.sleep(2)

#driver.find_element(By.LINK_TEXT,"Open Google").click()
#time.sleep(2)

#driver.find_element(By.PARTIAL_LINK_TEXT,"Bottom").click()
#time.sleep(2)

# Handling simple alert option
simple_alert=driver.find_element(By.XPATH,"//button[text()='Simple Alert']")
simple_alert.click()
time.sleep(2)

popup = Alert(driver)
print("Simple Alert text: ", popup.text)
popup.accept()
time.sleep(2)

# Handling confirm alert option

confirm_alert= driver.find_element(By.XPATH,"//button[text()='Confirm Alert']")
confirm_alert.click()
time.sleep(2)

c_popup=Alert(driver)
print("Confirm Alert text:", c_popup.text)
c_popup.dismiss()

'''
# Handling prompt alert option - ISsue with this alert on UI

prompt_alert=driver.find_element(By.XPATH,"//button[text()='Prompt Alert']")
prompt_alert.click()

p_popup=Alert(driver)
print("Prompt Alert:", p_popup.text)
p_popup.send_keys("Automation Learning")
time.sleep(5)
print("Prompt Alert 2:", p_popup.text)
p_popup.accept()

'''
#Upload file

driver.find_element(By.ID,"fileUpload").click()

'''
# Relative xpath: and operator method - Enabled & Disabled Fields
driver.find_element(By.XPATH,"//input[@type='text' and @value='Enabled']")
time.sleep(2)

#Relative xpath: or operator method - Enabled & Disabled Fields
driver.find_element(By.XPATH,"//input[@id='disabledInput' or @value='Disabled']")
time.sleep(2)

'''
