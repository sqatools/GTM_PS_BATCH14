
import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#initialize the Chrome driver
driver=webdriver.Chrome()
#maximize the browser window
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/dummy-booking-website/#google_vignette")

def handle_dropdown_using_select_by_value():
    passenger_dropdown=driver.find_element(By.ID , "admorepass")
    #create a select object
    time.sleep(10)
    select_passengers=Select(passenger_dropdown)
    #select option by visible value
    time.sleep(10)
    #select_passengers.select_by_value("2")
    #select_passengers.select_by_visible_text("Add 2 more passenger (200%)")
    select_passengers.select_by_index(2)
    print("Selected passengers using select_by_index:  Add 1 more passenger (100%) ")
handle_dropdown_using_select_by_value()      

def muilti_dropdown_example():
    time.sleep(10)
    multi_select_dropdown=driver.find_element(By.ID, "billing_country")
    #create a select object
    select_multi=Select(multi_select_dropdown)
    #select multiple options
    time.sleep(10)
    select_multi.select_by_value("AF")
    select_multi.select_by_visible_text("Algeria")
    print("Selected multiple options: Afghanistan and Algeria")
    
    

muilti_dropdown_example()






  

    

    