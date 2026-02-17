import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window
driver.implicitly_wait(20)

driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")


def handle_iframe():
    # get iframe element
    iframe_element = driver.find_element(By.NAME, "globalSqa")

    # switch to iframe
    driver.switch_to.frame(iframe_element)

    # get element with reference inside the iframe.
    heading_elem = driver.find_element(By.XPATH, "//div[@class='page_heading']/h1")
    print("heading name :", heading_elem.text)

    driver.find_element(By.ID, "mobile_menu_toggler").click()
    time.sleep(5)

    # switch to main content :  come out of the iframe and interact with main content
    driver.switch_to.default_content()


    heading_elem_main = driver.find_element(By.XPATH, "//div[@class='page_heading']/h1")
    print("main heading name :", heading_elem_main.text)


handle_iframe()


