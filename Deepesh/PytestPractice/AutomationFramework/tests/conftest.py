from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

# fixture to initialize the WebDriver and provide it to test classes
@pytest.fixture(scope="class")
def get_driver(request):
    opt = Options()
    opt.add_argument('--headless')
    driver = webdriver.Chrome(options=opt)
    driver.maximize_window()
    # class variable as driver, that we can 
    # access inside as self.driver
    request.cls.driver = driver
    yield
    driver.quit()