#login to website
import selenium
from selenium import webdriver  
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
username_field = driver.find_element(By.NAME, "username").send_keys("Admin")
password_field = driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

my_info_tab = driver.find_element(By.LINK_TEXT, "My Info").click()
first_name = driver.find_element(By.NAME, "firstName").clear()
first_name = driver.find_element(By.NAME, "firstName").send_keys("Hema")
last_name = driver.find_element(By.NAME, "lastName").clear()
last_name = driver.find_element(By.NAME, "lastName").send_keys("P") 
license_expiry_date = driver.find_element(By.XPATH, "//label[text()='License Expiry Date']/../following-sibling::div//input").send_keys("2026-12-31")
#(//input[@placeholder='yyyy-dd-mm'])[1]
dateof_birth = driver.find_element(By.XPATH, "//label[text()='Date of Birth']/../following-sibling::div//input").send_keys("1987-01-01")
#(//input[@placeholder='yyyy-dd-mm'])[2]
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='submit'])[1]")))
try:
    save_button = driver.find_element(By.XPATH, "(//button[@type='submit'])[1]")
    save_button.click()
except selenium.common.exceptions.ElementClickInterceptedException:
    driver.execute_script("arguments[0].click();", save_button)
#
save_button = driver.find_element(By.XPATH, "(//button[@type='submit'])[1]").click()

time.sleep(20)
driver.quit()