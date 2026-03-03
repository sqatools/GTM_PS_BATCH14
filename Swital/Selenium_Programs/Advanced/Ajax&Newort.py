from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    driver = webdriver.Chrome()
    try:
        driver.maximize_window()
        driver.get("https://sqatools.in/automation-practice-page/")
        wait = WebDriverWait(driver, 10)
        # ---------------- AJAX Success & Network Failure ----------------
        # Click 'Load Success' and verify loader text
        success_btn = driver.find_element(By.XPATH, "//button[contains(@onclick,'loadAjax(true)')]")
        success_btn.click()
        wait.until(EC.text_to_be_present_in_element((By.ID, "loader"), "Data loaded successfully!"))

        # Click 'Simulate Network Failure' and verify loader text
        failure_btn = driver.find_element(By.XPATH, "//button[contains(@onclick,'loadAjax(false)')]")
        failure_btn.click()
        wait.until(EC.text_to_be_present_in_element((By.ID, "loader"), "Network Error (500)"))
    finally:
        driver.quit()


if __name__ == "__main__":
    main()