from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")

def implicit_wait():
    driver.implicitly_wait(10)
t1 = time.time()
try:
    un = driver.find_element(By.ID, "username1")
    un.send_keys("12, john street, new york, usa")
except Exception as e:
    print("The raise exception is: ", e)
    raise
finally:
    t2= time.time()
    print(f"The actual took time: {t2 - t1}sec")

implicit_wait()