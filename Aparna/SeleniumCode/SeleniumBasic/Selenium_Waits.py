"""
1. implicit_wait
The implicit wait is a global wait that applies to all elements in the WebDriver instance.
When you set an implicit wait, the WebDriver will poll the DOM for a specified amount of time when trying to find an element if it is not immediately available. If the element is found within the specified time, 
it will be returned; otherwise, 
a NoSuchElementException will be thrown.
In the above code, we set an implicit wait of 10 seconds using driver.implicitly_wait(10). This means that if any element is not found immediately, 
the WebDriver will wait up to 10 seconds for it to become available before throwing an exception.

2. Explicit Wait
Explicit wait is a more flexible wait mechanism that allows you to wait for specific
conditions to be met before proceeding with the next steps in your test script.
With explicit wait, 
--you can specify a condition to wait for, such as the presence of an element,
the visibility of an element, or the clickability of an element.

3. Fluent Wait
Fluent wait is a more advanced form of explicit wait that allows you to specify the polling frequency
and the exceptions to ignore while waiting for a condition to be met.
e.g., you can specify that the WebDriver should check for the presence of an element every 500 milliseconds and
ignore NoSuchElementException while waiting.

4. static wait
Static wait is a simple wait mechanism where you specify a fixed amount of time to wait
before proceeding

1q  qwith the next steps in your test script. This is typically done using time.sleep() in Python.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



#initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")

#1.creating an function to demonstrate implicit wait
def implicit_wait_example():
    driver.implicitly_wait(10)
    t1=time.time()
    try:
        #try to find an element that is not immediately available
        element=driver.find_element(By.XPATH, "//textarea[@name='address1']")
        element.send_keys("Hello automation  testing")
        print("Implicit Wait: Element found and text entered.")
    except Exception as e:
        print("Implicit Wait: Element not found within the given time.", e)
        raise #raise the exception at particular line where it is occurred
    finally: #finally block will execute regardless of whether an exception is raised or not, ensuring that the time taken for the implicit wait is always calculated and printed.
        t2=time.time()
        print(f"Implicit Wait Time Taken: {t2-t1} seconds")
        
#implicit_wait_example()


def explicit_wait_example():

    # 2. Explicit Wait
    wait = WebDriverWait(driver, 15, poll_frequency=1)  # seconds
    t1 = time.time()
    try:
        element = wait.until(EC.presence_of_element_located((By.NAME, "address")))
        element.send_keys("456 Another St, City, Country")

        radio_button = wait.until(EC.element_to_be_clickable((By.ID, "male")))
        radio_button.click()

        java_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "java")))
        java_checkbox.click()

        print("Explicit Wait: Element found and text entered.")
    except Exception as e:
        print("Explicit Wait: Element not found within the given time.", e)
        raise
    finally:
        t2 = time.time()
        print(f"Explicit Wait Time Taken: {t2 - t1} seconds")


explicit_wait_example()