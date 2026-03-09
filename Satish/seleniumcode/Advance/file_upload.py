
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Edge() # Make driver of Edge webbrowser to interact with website
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/") # open this website

# Search file upload element

choose_file_element=driver.find_element(By.ID,'fileUpload')
#send file path to upload the file
choose_file_element.send_keys(r'C:\AutomationProject\github_guide.txt') # use r i.e. to make raw string to nullify effect of escape seq \n , \t etc
time.sleep(5)


"""
To upload randome name file everytime

# Upload a file in the original tab
    random_file_name = f"file_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    file_path = f"E:\\Filesdata\\Batch14\\{random_file_name}"
    # To create a sample file to upload because when we open file in write mode if there is no file of that name then it will create it
    with open(file_path, 'w') as f:
        f.write("This is a sample file for upload testing.")


    #driver.find_element(By.ID, "fileUpload").send_keys(r"E:\Filesdata\count_name.txt")
    driver.find_element(By.ID, "fileUpload").send_keys(file_path)

"""