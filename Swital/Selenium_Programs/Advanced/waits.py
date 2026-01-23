from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")


def implicit_wait():
    driver.implicitly_wait(10)
    t1 = time.time()
    try:
        un = driver.find_element(By.ID, "username")
        un.send_keys("Swital")
    except Exception as e:
        print("The raise exception is: ", e)
        raise
    finally:
        t2= time.time()
        print(f"The actual took time: {t2 - t1}sec")

#implicit_wait() 

def explicit_wait():
    wait = WebDriverWait(driver, 15)
    t1 = time.time()
    try:
        time.sleep(2)
        un = wait.until(EC.presence_of_element_located((By.ID, "username")))
        un.clear()
        un.send_keys("Swital")
    except Exception as e:
        print("The raise exception is: ", e)
        raise
    finally:
        t2= time.time()
        print(f"The actual took time: {t2 - t1}sec")

# explicit_wait()

def Fluent_wait():
    wait = WebDriverWait(driver, 10, poll_frequency=1)
    t1 = time.time()
    try:
        time.sleep(2)
        un = wait.until(EC.presence_of_element_located((By.ID, "username")))
        un.clear()
        un.send_keys("Swital")
    except Exception as e:
        print("The raise exception is: ", e)
        raise
    finally:
        t2= time.time()
        print(f"The actual took time: {t2 - t1}sec")

Fluent_wait()