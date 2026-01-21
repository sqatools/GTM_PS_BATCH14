"""
1. Implicit Waits:- The Implicit Wait in Selenium is used to tell the web driver to wait for a certain amount of time before it throws a “No Such Element Exception” (When we find element like textbox ,button etc by driver.find_element so it wait until element found on webpage)
This wait is applied to all the elements means for each search call driver.find_element it consider same wait time.
syntax:

from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)   # wait up to 10 seconds for any element
driver.get("https://example.com")

element = driver.find_element("id", "username")

How it works:

Selenium keeps polling the DOM for up to 10 seconds.

If the element appears earlier, it proceeds immediately.

If not found within 10 seconds → exception.
The DOM is a tree-like structure that represents all the elements of a web page in memory.

2. Explicit waits:
Explicit waits are used to wait for a specific condition to occur for specific element before proceeding further
in the code.This wait is applied to a specific element or condition and is not global(means same wait for all element) like implicit waits.
You can specify the maximum amount of time to wait for a condition, as well as the condition
itself (e.g., element to be clickable, presence of an element, visibility of an element, etc.).
Syntax:
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com")

wait = WebDriverWait(driver, 15) # Making object of WebDriverWait class
element = wait.until(
    EC.visibility_of_element_located((By.ID, "username"))
)

Common Conditions:

EC.presence_of_element_located((By.ID, "username"))
EC.visibility_of_element_located((By.ID, "username"))
EC.element_to_be_clickable((By.ID, "submit"))
EC.title_contains("Dashboard")
EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1"))


How it works:

Polls every 0.5 sec (default) # Means check availability element

Stops as soon as the condition is met

Throws TimeoutException if not met within given time

3. Fluent Waits: It is same as Explicit wait but it is advance Explicit wait and in this wait we can control polling frequency(after how many sec selenium check for element availability). However polling frequency is 0.5 sec fixed in Explicit wait.

4. Static waits:
    -> Static waits are the simplest form of waits where you simply pause the execution of the code for a
       fixed amount of time using functions like time.sleep() in Python.

    -> This type of wait does not depend on any condition and is generally not recommended for production
       code as it can lead to inefficient test execution.


"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Edge()   # Webdriver is a package and Edge is a class and we have make object driver

driver.get("https://sqatools.in/automation-practice-page/")
driver.maximize_window() ## maximize the browser window

# Implicit wait Example

def implicit_wait_example():
    driver.implicitly_wait(10)  # 10sec wait until element found on webpage when we find element by driver.find_element
    t1=time.time() # time.time() gives us current time in seconds
    try:
        element=driver.find_element(By.ID,'username') # Finding username text box element by its ID=usrname
        element.send_keys("satish")
        print("Element found and text entered")
    except Exception as e:
        print("Element not found within the given time",e)

    finally:
        t2=time.time()
        print(f"Implicit wait time taken to load element is {t2-t1}") #Implicit wait time taken to load element is 0.174025297164917

#implicit_wait_example() # Calling function

# Explicit Wait Example

def explicit_wait_example():
    wait= WebDriverWait(driver,10)
    t1=time.time()
    try:
        element=wait.until(EC.presence_of_element_located((By.ID,'username')))
        element.send_keys('satish')
        print("Element found and text entered")
    except Exception as e:
        print("Element not found within the given time", e)

    finally:
        t2=time.time()
        print(f"Explicit wait time taken to load element is {t2-t1}") #Explicit wait time taken to load element is 0.1727461814880371



explicit_wait_example() # Calling function








