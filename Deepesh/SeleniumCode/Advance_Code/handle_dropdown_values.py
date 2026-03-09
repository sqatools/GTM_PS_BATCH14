import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# initialize the Chrome driver
driver = webdriver.Chrome()
# maximize the browser window
driver.maximize_window()
driver.implicitly_wait(10)
# navigate to the URL
driver.get("https://sqatools.in/automation-practice-page/")

# Handling Dropdown using Select class
def handle_dropdown_using_select_by_label():
    country_dropdown = driver.find_element(By.ID, "country")
    # Create a Select object
    select_country = Select(country_dropdown)
    # Select option by visible text
    select_country.select_by_visible_text("India")
    print("Selected Country using select_by_visible_text: India")
    time.sleep(10)

#handle_dropdown_using_select_by_label()


def handle_dropdown_using_select_by_option_value():
    country_dropdown = driver.find_element(By.ID, "country")
    # Create a Select object
    select_country = Select(country_dropdown)
    # Select option by select_by_value
    select_country.select_by_value("uk")
    print("Selected Country using select_by_value: India")
    time.sleep(10)

#handle_dropdown_using_select_by_option_value()

def handle_dropdown_using_select_by_index():
    country_dropdown = driver.find_element(By.ID, "country")
    # Create a Select object
    select_country = Select(country_dropdown)
    # Select option by index
    select_country.select_by_index(4)  # 
    print("Selected Country using select_by_index: Australia")
    time.sleep(10)

#handle_dropdown_using_select_by_index()

def select_multiple_options_in_multiselect_dropdown():
    multi_select_dropdown = driver.find_element(By.ID, "skills")
    # Create a Select object
    select_multi = Select(multi_select_dropdown)
    # Select multiple options
    select_multi.select_by_visible_text("Python")
    select_multi.select_by_visible_text("Selenium")
    select_multi.select_by_index(2)  # Playwright
    print("Selected multiple options in multi-select dropdown: Python, Selenium, Playwright")
    time.sleep(10) 

    select_multi.deselect_by_visible_text("Selenium")
    print("Deselected option: Selenium")

    time.sleep(10)
    select_multi.deselect_all()
    print("Deselected all options in multi-select dropdown")
    time.sleep(10)



select_multiple_options_in_multiselect_dropdown()
# https://automationexercise.com/