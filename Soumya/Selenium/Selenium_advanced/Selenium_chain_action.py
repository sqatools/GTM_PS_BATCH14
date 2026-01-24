import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
action = ActionChains(driver)



def perform_drag_drop_operation():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    iframe_elem = driver.find_element(By.XPATH, "//iframe[contains(@src, 'photo-manager')]")
    driver.switch_to.frame(iframe_elem)

    img1 = driver.find_element(By.XPATH, "//h5[text()='High Tatras 2']/parent::li")
    trash_bin = driver.find_element(By.ID, "trash")

    # perform drag and drop
    action.drag_and_drop(img1, trash_bin).perform()
    print("Drag and drop operation performed successfully.")

    time.sleep(10)



#perform_drag_drop_operation()

def perform_drag_drop2():
    driver.get("https://sqatools.in/automation-practice-page/")
    time.sleep(10)
    image1 = driver.find_element(By.CSS_SELECTOR, "div.drag")
    print(image1.text)
    target1 = driver.find_element(By.CSS_SELECTOR, "div.drop")
    print(target1.text)
    time.sleep(5)
    action.click_and_hold(image1).move_to_element(target1).release().perform()
    #Alternatively, you can use:
    #action.drag_and_drop(image1, target1).perform()
    print("Drag and drop operation 2 performed successfully.")
    time.sleep(10)

#perform_drag_drop2()

def perform_hover_to_element():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    time.sleep(5)
    testers_hub = driver.find_element(By.XPATH, "//div[@id='menu']//a[contains(text(), 'Teste')]")
    action.move_to_element(testers_hub).perform()
    time.sleep(5)

    demo_site_testing = driver.find_element(By.XPATH, "//div[@id='menu']//span[contains(text(), 'Demo Testing Site')]")
    action.move_to_element(demo_site_testing).perform()
    time.sleep(5)

    alerts_link = driver.find_element(By.XPATH, "//div[@id='menu']//span[contains(text(), 'AlertBox')]")
    action.move_to_element(alerts_link).click().perform()
    time.sleep(5)

perform_hover_to_element()