
import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    country_dropdown = driver.find_element(By.ID, "billing_country")
    select_country = Select(country_dropdown)
    time.sleep(10)
    print("is multiple:", select_country.is_multiple)

    if select_country.is_multiple:
        select_country.select_by_value("AF")
        select_country.select_by_visible_text("Algeria")
        select_country.select_by_visible_text("Åland Islands")
        select_country.select_by_visible_text("American Samoa")
        select_country.select_by_visible_text("Angola")
        time.sleep(10)
        print("Selected multiple options: Afghanistan, Algeria, Åland Islands, American Samoa and Angola")
        select_country.deselect_all()
        print("Deselected all selected options because the dropdown is multi-select.")
    else:
        print("This dropdown is NOT multi-select. You cannot deselect on a single-select dropdown.")
        print("Instead, change the selected option using select_by_index() or select_by_visible_text().")
        # Example: select another option to change the selection
        select_country.select_by_index(0)
        print("Changed selection to index 0 instead of deselecting.")

    print("Current selected option:", select_country.first_selected_option.text)
    print("All selected options:", [option.text for option in select_country.all_selected_options])

    """
    wait=WebDriverWait(driver, 10)
    t1=time.time()
    try:
        wait.until(EC.text_to_be_present_in_element_value("AF"))
        print("Option with value 'AF' is deselectable.")
    except Exception as e:
        print("Option with value 'AF' is not deselectable within the given time.", e)
        raise
    finally:
        t2=time.time()
        print(f"Time taken to check deselectable: {t2-t1} seconds")

    """

muilti_dropdown_example()


