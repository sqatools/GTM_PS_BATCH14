from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
driver.get("https://sqatools.in/automation-practice-page/")

# 1️⃣ Locate outer shadow host
shadow_host = driver.find_element(By.ID, "shadow-host")

# 2️⃣ Get outer shadow root
shadow_root1 = shadow_host.shadow_root

# 3️⃣ Locate inner shadow host
inner_host = shadow_root1.find_element(By.ID, "inner-host")

# 4️⃣ Get inner shadow root
shadow_root2 = inner_host.shadow_root

# 5️⃣ Locate input inside nested shadow root
shadow_input = shadow_root2.find_element(By.ID, "shadowInput")

# 6️⃣ Enter text
shadow_input.send_keys("Hello Swital")

time.sleep(3)
driver.quit()