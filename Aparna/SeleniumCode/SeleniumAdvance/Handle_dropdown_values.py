
"""dropdown methods
1. select_by_visible_text
2. select_by_value
3. select_by_index
4. deselect_by_visible_text
5. deselect_all

practices for handling dropdowns:# https://automationexercise.com/
"""

from selenium import webdriver
from selenium.webdriver.common.by import By     
from selenium.webdriver.support.select import Select
import time


#initialize the Chrome driver
driver = webdriver.Chrome()
#maximize the browser window
driver.maximize_window()
driver.implicitly_wait(10) # set implicit wait for 10 seconds
#navigate to the practice page
driver.get("https://sqatools.in/automation-practice-page/")

#handle dropdown using Select class
def handle_dropdown_using_select_by_label():
    time.sleep(10)
    country_dropdown=driver.find_element(By.ID,"country")
    #create a Select object
    select_country=Select(country_dropdown)
    #select option by visible text
    time.sleep(10)
    select_country.select_by_visible_text("India")
    print("Selected Country using select_by_visible_text: India")
    
#handle_dropdown_using_select_by_label()

def handle_dropdown_using_select_by_option_value():
    country_dropdown=driver.find_element(By.ID, "country")
    #create a Select object
    select_country=Select(country_dropdown)
    #select option by select_by_value
    select_country.select_by_value("usa")
    time.sleep(10)
    print("Selected Country using select_by_value: usa")

#handle_dropdown_using_select_by_option_value()

def handle_dropdown_using_select_by_index():
    coutry_dropdown=driver.find_element(By.ID, "country")
    #create a Select object
    select_country=Select(coutry_dropdown)
    #select option by index
    select_country.select_by_index(3)  # Australia
    time.sleep(10)  
    print("Selected Country using select_by_index: UK")
    
#handle_dropdown_using_select_by_index()


def select_multiple_options_in_multiselect_dropdown():
    multi_select_dropdown=driver.find_element(By.ID, "skills")
    #create a Select object
    select_multi=Select(multi_select_dropdown)
    #select multiple options
    select_multi.select_by_visible_text("Python")
    select_multi.select_by_visible_text("Selenium")
    select_multi.select_by_index(3)  # API Testing
    time.sleep(10)
    print("Selected multiple options in multi-select dropdown: Python, Selenium, API Testing")
    
    #deselect one option--selenium
    select_multi.deselect_by_visible_text("Selenium")
    print("Deselected option: Selenium")
    
    #deselect all options
    select_multi.deselect_all()
    print("Deselected all options in multi-select dropdown")
    time.sleep(10)
        
select_multiple_options_in_multiselect_dropdown()