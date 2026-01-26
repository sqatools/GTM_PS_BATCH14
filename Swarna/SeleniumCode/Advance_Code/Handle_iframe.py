import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")

def handle_iframe():
    iframe_element = driver.find_element(By.NAME, "globalSqa")

    # switch to iframe
    driver.switch_to.frame(iframe_element)

    # get element with reference inside the iframe
    heading_elem = 