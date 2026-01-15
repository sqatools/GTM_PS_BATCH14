"""
Selenium Locators:
    ID :# covered 
    XPATH 
    LINK_TEXT# covered
    PARTIAL_LINK_TEXT #  covered
    NAME #: covered
    TAG_NAME #  covered
    CLASS_NAME 
    CSS_SELECTOR 

"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# initialize the Chrome driver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")
# Using different locators to find elements
# GET By ID
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("Hema")

# GET By NAME
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("Hema123")
address_textarea = driver.find_element(By.NAME, "address")
address_textarea.clear()
address_textarea.send_keys("Sargam, Pune  Maharashtra India")

# GET By XPATH
radio_button = driver.find_element(By.XPATH, "//input[@value='female']")
radio_button.click()
time.sleep(10)

# GET By LINK_TEXT
link_element = driver.find_element(By.LINK_TEXT, "Python Basic Programs")
link_element.click()
time.sleep(5)

# GET By PARTIAL_LINK_TEXT
partial_link_element = driver.find_element(By.PARTIAL_LINK_TEXT, "Python If-Else")
partial_link_element.click()
time.sleep(5)

#driver.close()

# GET by absolute XPATH and relative XPATH
"""link_pythonLoopPrograms = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/main/article/div/div/section[4]/ul/li[4]/a")
link_pythonLoopPrograms.click()
time.sleep(5)"""

link_python_StringPrograms = driver.find_element(By.XPATH, "//ul[@class='wp-block-list']/li/a[text()='Python String Programs']")
link_python_StringPrograms.click()
time.sleep(5)
driver.close()
"""
What is XPath?
XPath (XML Path Language) is a query language used to navigate and select nodes from an XML

There are two main types of XPath:
1. Absolute XPath: It defines the path from the root element to the desired element. 
   It starts with a single slash (/). For example, /html/body/div[1]/h1.
   e.g. 
   ->  /html/body/div[1]/div/div[1]/main/article/div/header/h1
   -> /html/body/div[1]/div/div[1]/main/article/div/div/section[1]/h2

2. Relative XPath: It defines the path from the current node to the desired element. 
  It starts with a double slash (//). For example, 
    e.g. //taganame[@attribute='value'] or //*[@attribute='value']
    -> //h1[@id='header'].
    -> //h1[@class='entry-title']  or  //*[@class="entry-title"]
    -> //h1[@itemprop="headline"]
    -> //input[@placeholder="Enter username"]
    -> //input[@placeholder="Enter password"]
    -> //button[@type="submit"]

Relative Xpath Methods:
1. text() Method: This method is used to select elements based on their text content.
   e.g. //tagname[text()='textvalue']
   -> //h2[text()='XPath Syntax']
   -> //ul[@class='wp-block-list']/li/a[text()='Python Basic Programs']
   -> //button[text()='Confirm Alert']
   -> //td[text()='Deepesh']
   -> //input[@id="fileUpload"]


2. contains() Method: This method is used to select elements that contain a specific substring in their attribute value or text content.
   e.g. //tagname[contains(@attribute,'substring')] or 
        //tagname[contains(text(),'substring')]

    -> //h1[contains(@class, "entry")]
    -> //h1[contains(text(), 'Automation Practice Page')]
    -> (//h1[contains(text(), 'Automation Practice Page')])[1]"""