from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

driver = webdriver.Chrome()
driver.get("https://sqatools.in/automation-practice-page/")
driver.maximize_window()
time.sleep(2)

# Locate all table rows (tbody > tr)
rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

table_data = []

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = [cell.text for cell in cells]
    table_data.append(row_data)

# Write to CSV
with open("Swital/Selenium_Programs/Advanced/web_table_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(["ID", "Name", "Role"])
    
    # Write rows
    writer.writerows(table_data)

print("Data successfully written to CSV!")

driver.quit()