import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
driver.implicitly_wait(10)

title= driver.title
print("Page Title:", title)

prompt_alert=driver.find_element(By.ID,"promptbtn")
prompt_alert.click()

p_popup=Alert(driver)
print("Prompt Alert:", p_popup.text)
p_popup.send_keys("Sara")
time.sleep(10)
p_popup.accept()

message= driver.find_element(By.ID,"prompt")
print("Prompt Alert Message:", message.text)
