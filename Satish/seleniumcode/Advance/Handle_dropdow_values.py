import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select # Import Select class

driver=webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/automation-practice-page/")

# Handling Dropdown using Select class

# First we search Dropdown(Select) element on above webpage
dropdown_element=driver.find_element(By.ID,'country')
#Create a select object
select_object=Select(dropdown_element) # Provide web element name in Select Class
# Select option by visible text
#select_object.select_by_visible_text('India')
#We can select option By value also as below
#select_object.select_by_value('india')
#We can select option By index also also as below
select_object.select_by_index(1)

time.sleep(5)

# Handle MultiSelect Dropdown (we can select more than one value at a time) in above website

def multi_select_dropdown():
    # First we search Multi Select Dropdown element on above webpage
    multi_select_dropdown_element=driver.find_element(By.ID,'skills')
    # Create a select object
    multi_select_object=Select(multi_select_dropdown_element)
    multi_select_object.select_by_visible_text('Python')
    multi_select_object.select_by_visible_text('Selenium')
    multi_select_object.select_by_visible_text('Playwright') # We have selected three option together
    time.sleep(5)
    multi_select_object.deselect_by_visible_text('Selenium') # We have deselect Selenium option
    time.sleep(5)

multi_select_dropdown()

# https://automationexercise.com/ Website for practise





