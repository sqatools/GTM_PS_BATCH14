
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from Deepesh.SeleniumCode.Basic.first_Selenium_methods import java_checkbox

driver=webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/automation-practice-page/")

# Selenium Methods:
# get the title of the page
title=driver.title
print("page title:",title) #page title: Automation Practice Page - SQA Tools

# get the current URL of the page
current_url=driver.current_url
print("current url",current_url) #https://sqatools.in/automation-practice-page/


# # get the page source i.e. HTML code
# page_source=driver.page_source
# print("page source",page_source)


# get text from an element
#suppose we want text of Automation Page
heading_element=driver.find_element(By.CLASS_NAME,"entry-title")
heading_element_text=heading_element.text
print("text",heading_element_text) #text Automation Practice Page

# get attribute value from an element
# Suppose we want to get attribute of link text Python Basic ProgramS
# first we will find first element on website
link_element=driver.find_element(By.XPATH,"//ul[@class='wp-block-list']//a[text()='Python Basic Programs']")
# we use // for grand children .ul is a parent and tag a is grand children of ul

# Now we want to get value of attribute href
attribute_value=link_element.get_attribute("href")
print("Attribute value",attribute_value) #Attribute value https://sqatools.in/python-basic-programs/

# checke element  is enabled or not

# In given website there are two textbox one is Enabled and other id disabled under Enabled/Disabled field
#we want to check these element whether they are enable or disable by selenium method

# first we find that elemnt and then apply method
enabled_element=driver.find_element(By.ID,'enabledInput')
print(enabled_element.is_enabled()) #True
disabled_element=driver.find_element(By.ID,'disabledInput')
print(disabled_element.is_enabled()) #False

# check element is displayed or not
# displayed means visible or not . Under Hidden Element , textbox is invisible

hidden_element=driver.find_element(By.ID,'hiddenField')
print("Hidden Element",hidden_element.is_displayed()) #Hidden Element False

# check element is selected or not
# Check status of Checkboxes (Java,Python,Selenium) on website
Java_checkbox=driver.find_element(By.ID,'java')
print("Status of Java Checkbox",Java_checkbox.is_selected()) #Status of Java Checkbox False

# Now we check Java checkbox and check staus again
Java_checkbox.click()
print("After clicking Status of Java Checkbox",Java_checkbox.is_selected()) #After clicking Status of Java Checkbox True


# forward and backward navigation i.e. open one webpage and come back to previous webpage

# suppose we click on link Python Loop Programs to open other webpage and again come back previous page

# first we find element ofn web page i.e. link(Python Loop Programs)
link_python_loop_programs=driver.find_element(By.XPATH,"//a[text()='Python Loop Programs']")
print("Before clicking link",driver.save_screenshot('before_clicking.png'))
# Now click on link to open other webpage
link_python_loop_programs.click()
print("After clicking link",driver.save_screenshot('after_clicking.png'))
# Now move back
driver.back()
print("After moving back",driver.save_screenshot('moving_back.png'))