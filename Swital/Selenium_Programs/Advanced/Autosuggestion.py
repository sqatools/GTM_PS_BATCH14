"""Simple autosuggestion example: type into the search box and click the first suggestion."""
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

        # type to trigger suggestions
        input_field = driver.find_element(By.ID, "searchBox")
        input_field.clear()
        input_field.send_keys("Selenium")

        # wait for first suggestion and click it
        wait = WebDriverWait(driver, 10)
        first = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#suggestions div")))
        first.click()

        time.sleep(2)  # pause so you can see the result
    finally:
        driver.quit()


if __name__ == "__main__":
    main()