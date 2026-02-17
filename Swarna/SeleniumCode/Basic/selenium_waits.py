"""
1. Implicit waits
- Implicit waits are used to tell the WebDriver to poll the DOM for a certain amount to get 
    element from the web page.
- This wait is set for the life of the WebDriver instance and will apply to all elements found 
    using the WebDriver.

2. Explicit Waits: 
    -> Explicit waits are used to wait for a specific condition to occur before proceeding further
       in the code.

    -> You can specify the maximum amount of time to wait for a condition, as well as the condition
       itself (e.g., element to be clickable, presence of an element, visibility of an element, etc.).

    -> This wait is applied to a specific element or condition and is not global like implicit waits.

3. Fluent Waits:
    Fluent waits are a more advanced form of explicit waits that allow you to define the maximum amount
    to locate the element for, the frequency with which to check for the element, and to ignore specific types

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

# initialize the Crome driver
driver = webdriver.Chrome()
# maximize the browser window
driver.maximize_window()
# navigate to the URL
driver.get("https://sqatools.in/automation-practice-page/")

def implicit_wait_example():
    # 1. Implicit Wait
    driver.implicitly_wait(10)
    # Try to find an element that may take time to load
    t1 = time.time()
    try:
        element = driver.find_element(By.)