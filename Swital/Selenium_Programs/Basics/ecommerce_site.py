from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://int.zigzag.lk/collections/blazers-jackets")
driver.implicitly_wait(10)
#style_size_checkbox = driver.find_element(By.XPATH, "(//span[text() = 'STYLE SIZE ']/following::label//span[@class='position-relative d-block mr-8 border'])[1]")
style_size_checkbox = driver.find_element(By.XPATH, "(//span[text() = 'STYLE SIZE ']/following::label//span[text() = 'XS'])[1]")
style_size_checkbox.click()
time.sleep(2)