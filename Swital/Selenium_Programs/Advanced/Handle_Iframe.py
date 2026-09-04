from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")

# first find the iframe element: start with tagname 'iframe' for the locating  element, 
# inside that iframe tagname we need find and locate element first to work with iframe
iframe_element = driver.find_element(By.NAME, "globalSqa")

# Switch to iframe using web element
driver.switch_to.frame(iframe_element)
iframe = driver.find_element(By.XPATH, "//div[@class='page_heading']")
print("Iframe Heading Text is :", iframe.text)

#switch back to main content
driver.switch_to.default_content()
time.sleep(3)

# locate the main page element
iframe_main = driver.find_element(By.XPATH, "//div[@class='page_heading']")
print("Main Heading Text is :", iframe_main.text)