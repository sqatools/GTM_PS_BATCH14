from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")

# TextFields
username = driver.find_element(By.ID, "username")
username.send_keys("Swital")
password = driver.find_element(By.XPATH, "//input[@type='password']")
password.send_keys("ABC@123")
address = driver.find_element(By.XPATH, "//textarea[text()='Enter address']")
address.clear()
address.send_keys("12.4, Abc street, india")

# RadioButton
#radio_btn = driver.find_element(By.XPATH, "//input[@type='radio']/following-sibling::label[text()='Male']")
#radio_btn.click()
time.sleep(2)

#Another way to select one radio button using loop using function
def select_radio_by_label(driver, label_text):
    radios = driver.find_elements(By.XPATH, "//input[@type='radio']")
    for radio in radios:
        label = radio.find_element(
            By.XPATH, "following-sibling::label | parent::label"
        ).text.strip()

        if label.lower() == label_text.lower():
            if not radio.is_selected():
                radio.click()
            break

#select_radio_by_label(driver, "female")

# select radio button one by one
radio_btns = driver.find_elements(By.XPATH, "//input[@type='radio']")
for rb in radio_btns:
    rb.click()
    time.sleep(1)

# Checkboxs selection
# single checkbox selection:
#checkbox = driver.find_element(By.ID, "java")
#checkbox.click()
#time.sleep(1)


# multiple selection
checkboxes = driver.find_elements(By.XPATH, "//h2[text()='Checkboxes']/following::input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()
    time.sleep(2)

