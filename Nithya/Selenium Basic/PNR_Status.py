import time
from webbrowser import Chrome   
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.confirmtkt.com/")
driver.find_element(By.XPATH, "//li//a[contains( text(), 'PNR Status')]").click()
time.sleep(1)   
#a= input("Enter the PNR number: ")
driver.find_element(By.XPATH, "//input [@id='inputPnrWeb']").click()
driver.find_element(By.XPATH, "//input [@id='inputPnrWeb']").send_keys("4939069101")
driver.find_element(By.XPATH, "//div//button[@id= 'checkPnrWeb']").click()
time.sleep(1)
driver.save_screenshot("PNR_Status.png")
time.sleep(5)