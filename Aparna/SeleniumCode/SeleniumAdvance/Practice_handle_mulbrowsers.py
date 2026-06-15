from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime


driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/p/home.html")

#handle browser tab 
#open new tab navigate to manual testing 
driver.find_element(By.PARTIAL_LINK_TEXT,"Manual Testing").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"What is Software Testing").click()
time.sleep(5)

#get all windowa handles
windows_list=driver.window_handles
print(windows_list)

driver.switch_to.window(windows_list[1])
print("New tab title:", driver.title)

driver.switch_to.window(windows_list[0])

driver.find_element(By.PARTIAL_LINK_TEXT,"Methods").click()
print("present tab title :", driver.title)

driver.switch_to.window(windows_list[1])
print("Previous tab tittle:", driver.title)



