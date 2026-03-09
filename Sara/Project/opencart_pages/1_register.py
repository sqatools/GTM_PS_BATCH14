import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#initiating edge driver
driver = webdriver.Chrome()

# maximizing edge browser
driver.maximize_window()

#navigating to url
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)

#get title of the page.
title= driver.title
print ("Title of the page:", title)

#get url of the pagr
current_url = driver.current_url
print("Current URL: ", current_url)

#login
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("admin123")

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)




