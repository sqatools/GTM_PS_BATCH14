from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/automation-practice-page/")

#Is Enabled and disabled
btn_enable = driver.find_element(By.ID, "normalButton")
print("Button is enable:", btn_enable.is_enabled())

# Disabled 
btn_disable = driver.find_element(By.ID, "disabledInput")
print("Button is Disabled:", btn_disable.is_enabled())

# Displayed 
print("Button is displyed:", btn_enable.is_displayed())

# Is selected
select = driver.find_element(By.ID, "java")
print("The checkbox is selcted or not:", select.is_selected())
select.click();
print("The checkbox is selcted:", select.is_selected())


# Navigation Method
driver.get("https://sqatools.in/")
time.sleep(4)
print("on page:", driver.title)
driver.back()
time.sleep(4)
print("back page:", driver.title)
driver.forward()
time.sleep(4)
print("forward page:", driver.title)
driver.refresh()
time.sleep(4)
driver.save_screenshot("refresh.png")