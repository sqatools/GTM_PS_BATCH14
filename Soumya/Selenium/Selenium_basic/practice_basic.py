"""
Docstring for Soumya.Selenium.Selenium_basic.selenium_basic_practice
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("https://sqatools.in/login-page/")
driver.find_element(By.ID, "email").send_keys("user1@gmail.com")
time.sleep(5)
driver.find_element(By.ID, "pass").send_keys("User@1234")
time.sleep(5)
driver.find_element(By.ID, "loginbutton").click()
time.sleep(10)
driver.close()

"""
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sqatools.in/dummy-booking-website/")
time.sleep(5)
driver.find_element(By.NAME, "firstname").send_keys("Soumya")
time.sleep(2)
driver.find_element(By.XPATH,"(//input[@id='firstname'])[2]").send_keys("Kumar")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='birthday']").send_keys("12/31/1990")
time.sleep(2)
driver.find_element(By.ID,"male").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//*[@id='admorepass'])").click()
time.sleep(5)
driver.find_element(By.XPATH,"(//a[text()='Login Page'])[1]").click()
time.sleep(5)
driver.close()
"""

"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com")
driver.find_element(By.XPATH, "//*[text()='A/B Testing']").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Elemental Selenium").click()
time.sleep(5)
driver.find_element(By.XPATH, "//button[text()='take me to the tips!']").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//button[@class='button button--primary'])[1]").click()
time.sleep(5)
driver.close()

"""

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com")
driver.find_element(By.XPATH, "//*[text()='A/B Testing']").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Elemental Selenium").click()
time.sleep(5)
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Take me to the tips!')]"))
)
element.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//button[@class='button button--primary'])[1]").click()
