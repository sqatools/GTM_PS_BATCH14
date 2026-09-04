from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/challenging_dom")

# Example of locating elements using different locators
# Locating the heading using TAG_NAME
heading = driver.find_element(By.TAG_NAME, "h3")
print("The heading is:", heading.text)
# Locating a paragraph using class name
#paragraph_class = driver.find_element(By.CLASS_NAME, "example")
#print("Paragraph text using class name:", paragraph_class.text)

# locating paragram by classname followed by tag name
#paragraph_class_tag = driver.find_element(By.CLASS_NAME, "example").find_element(By.TAG_NAME, "p")
#print("Paragraph text using class name followed by tag name:", paragraph_class_tag.text)

# Locating a paragraph using XPath
#paragraph_xpath = driver.find_element(By.XPATH, "//div[@class='example']/p")
#print("Paragraph text using XPath:", paragraph_xpath.text)

# Locating a paragraph using text
paragraph = driver.find_element(By.XPATH, "//p[contains(text(),'The hardest part')]")
print("Paragraph text:", paragraph.text)

baz_btn = driver.find_element(By.XPATH, "//a[contains(text(), 'baz')]")
baz_btn.click()
bar_btn = driver.find_element(By.XPATH, "//a[text()='bar']")
bar_btn.click()
qux_btn = driver.find_element(By.XPATH, "//a[@class='button success']")
qux_btn.click()
row_1st_test = driver.find_element(By.XPATH, "//td[text()= 'Iuvaret0']")
print("First row first column text is:", row_1st_test.text)
time.sleep(2)
edit_link = driver.find_element(By.XPATH, "(//a[contains(text(), 'edit')])[1]")
edit_link.click()
time.sleep(2)
delete_link = driver.find_element(By.XPATH, "(//a[@href='#delete'])[1]")
delete_link.click()
img = driver.find_element(By.ID, "canvas")
print("Image element found with ID 'canvas':", img.text)