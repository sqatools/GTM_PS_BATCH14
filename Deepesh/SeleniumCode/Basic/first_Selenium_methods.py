"""
install selenium using pip:
pip install selenium
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# initialize the Chrome driver
driver = webdriver.Chrome()

# maximize the browser window
driver.maximize_window()
# navigate to the URL
driver.get("https://sqatools.in/automation-practice-page/")
driver.implicitly_wait(10)

# Selenium Methods:
# get the title of the page
title = driver.title
print("Page Title:", title)

# get the current URL of the page
current_url = driver.current_url
print("Current URL:", current_url)


# get the page source
# page_source = driver.page_source 
# print("Page Source:", page_source)  # Uncomment to print the entire page source

# get text from an element
heading_element = driver.find_element(By.XPATH, "//header/h1")
print("Heading Text:", heading_element.text)


# get attribute value from an element
# get all the links from the page and print their href attributes
links = driver.find_elements(By.XPATH, "//ul[@class='wp-block-list']//a")
for link in links:
    href = link.get_attribute("href")
    print("Link Href:", href)



# checke element  is enabled or not

enable_input = driver.find_element(By.ID, "enabledInput")
disbaled_input = driver.find_element(By.ID, "disabledInput")

print("Is Enable Input Enabled?:", enable_input.is_enabled())
print("Is Disabled Input Enabled?:", disbaled_input.is_enabled())   

# check element is displayed or not
print("Is Enable Input Displayed?:", enable_input.is_displayed()) # True
print("Is Disabled Input Displayed?:", disbaled_input.is_displayed()) # True

hidden_element = driver.find_element(By.ID, "hiddenField")
print("Is Hidden Element Displayed?:", hidden_element.is_displayed()) # False

# check element is selected or not
java_checkbox = driver.find_element(By.ID, "java")
print("Is Java Checkbox Selected?:", java_checkbox.is_selected())  # False
java_checkbox.click()   
print("Is Java Checkbox Selected After Click?:", java_checkbox.is_selected())  # True


# forward and backward navigation
basic_program = driver.find_element(By.XPATH, "//ul[@class='wp-block-list']//a[text()='Python Basic Programs']")
# web element screenshot
basic_program.screenshot("before_click.png")
basic_program.click()
time.sleep(3)
driver.back()
# page screenshot
driver.save_screenshot("back_navigation.png")
time.sleep(3)
driver.forward()
driver.save_screenshot("forward_navigation.png")
time.sleep(3)


