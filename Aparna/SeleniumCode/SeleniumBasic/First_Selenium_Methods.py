import time

from selenium import webdriver
from selenium.webdriver.common.by import By



#initialize the Chrome driver
driver = webdriver.Chrome()
"""Implicity wait--By default, for each find_element or find_elements call, Selenium will wait
up to 0 seconds for the element to be present in the DOM. 
If the element is not found within that time, 
will throw a NoSuchElementException. By setting an implicit wait, 
you can specify a maximum amount of time to wait for an element to 
become available before throwing an exception."""
driver.implicitly_wait(10)

driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")

#Selenium Methods
#get the title of the page
title=driver.title
print("page title:", title)

#get the current URL of the page
current_url=driver.current_url
print("Current URL:", current_url)

#get the page source(to verify if a specific text or element is present in the page source)
#page_source=driver.page_source
#print("Page Source:", page_source) # if you want to print the entire page source, it may be very long. You can also print a portion of it if needed.
#print("Page Source Length:", len(page_source)) # Print the length of the page source

#get text from an element
heading_element=driver.find_element(By.XPATH, "//header/h1")
print("Heading Text:", heading_element.text)

#get attribute value from an elementf
#get all the links on the page and print their href attribute
links=driver.find_elements(By.XPATH, "//li//a[@class='wp-block-latest-posts__post-title']")
for link in links:
    #class=link.get_attribute("class")   
    href=link.get_attribute("href")
    print("Link Href:", href)
    time.sleep(2) 
    

# is selectable() method to check if an element is selectable or not
# is_displayed() method to check if an element is visible on the page or not

#check element is  enable  or not 
# is_enabled() method to check if an element is enabled or not
enable_input=driver.find_element(By.ID, "enabledInput")
"""if enable_input.is_enabled():
    print("The input field is enabled.")
else:
    print("The input field is disabled.")
    
disable_input=driver.find_element(By.ID, "disabledInput")
if disable_input.is_enabled():
    print("The input field is enabled.")
else:
    print("The input field is disabled.")
"""
print("Is Enable Input Enabled?:", enable_input.is_enabled())
disbaled_input=driver.find_element(By.ID, "disabledInput")
print("Is Disabled Input Enabled?:", disbaled_input.is_enabled())

#check element is displayed or not
print("Is Enable Input Displayed?:", enable_input.is_displayed()) # True
print("Is Disabled Input Displayed?:", disbaled_input.is_displayed()) # True

hidden_element=driver.find_element(By.ID, "hiddenField")
print("Is Hidden Element Displayed?:", hidden_element.is_displayed()) # False


#check element is selected or not
# is_selected() method to check if a checkbox or radio button is selected or not    
java_checkbox = driver.find_element(By.ID, "java")
print("Is Java Checkbox Selected?:", java_checkbox.is_selected())  # False
java_checkbox.click()   
print("Is Java Checkbox Selected After Click?:", java_checkbox.is_selected())  # True

Python_checkbox=driver.find_element(By.ID, "python")
print("Is Python Checkbox Selected?:", Python_checkbox.is_selected()) # False   
Python_checkbox.click() # select the checkbox
print("Is Python Checkbox Selected After Click?:", Python_checkbox.is_selected()) # True

Selenium_checkbox=driver.find_element(By.ID, "selenium")
print("Is Selenium Checkbox Selected?:", Selenium_checkbox.is_selected()) # False   
Selenium_checkbox.click() # select the checkbox
print("Is Selenium Checkbox Selected After Click?:", Selenium_checkbox.is_selected()) # True

#forward and backward navigation
typescript_oopspractice=driver.find_element(By.XPATH, "//ul[@class='wp-block-latest-posts__list wp-block-latest-posts']//a[text()='TypeScript OOPs Practice Questions with Explanations']")
typescript_oopspractice.click()

typescript_oopspractice.screenshot("before_click.png") # web element screenshot
time.sleep(3)
driver.back() # navigate back to the previous page
driver.save_screenshot("back_navigation.png") # page screenshot after navigating back
time.sleep(3)
driver.forward() # navigate forward to the next page    
driver.save_screenshot("forward_navigation.png") # page screenshot after navigating forward
time.sleep(3)