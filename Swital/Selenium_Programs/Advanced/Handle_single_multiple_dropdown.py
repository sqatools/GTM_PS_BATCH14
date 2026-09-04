from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://sqatools.in/automation-practice-page/")

# Single Dropdown using select class and its methods
def Handle_dropdown_label():
    dropdown_element = driver.find_element(By.ID, "country")
    select_obj = Select(dropdown_element)
    select_obj.select_by_visible_text("USA")
# Handle_dropdown_label()

# Single Dropdown using select class and its methods
def Handle_dropdown_value():
    dropdown_element = driver.find_element(By.ID, "country")
    select_obj = Select(dropdown_element)
    select_obj.select_by_value("usa")
#Handle_dropdown_value()

# Single Dropdown using select class and its methods
def Handle_dropdown_index():
    dropdown_element = driver.find_element(By.ID, "country")
    select_obj = Select(dropdown_element)
    select_obj.select_by_index(3)
#Handle_dropdown_index()

def Multidropdown_select():
    multi_dropdown_element = driver.find_element(By.ID, "skills")
    select_obj = Select(multi_dropdown_element)
    select_obj.select_by_visible_text("Python")
    select_obj.select_by_visible_text("Selenium")
    select_obj.select_by_index(3)

    time.sleep(2)
    select_obj.deselect_all()
    time.sleep(2)

Multidropdown_select()

