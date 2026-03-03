from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
# use webdriver-manager to auto-download chromedriver
from webdriver_manager.chrome import ChromeDriverManager

# fixture to initialize the WebDriver and provide it to test classes
@pytest.fixture(scope="class")
def get_driver(request):
    opt = Options()
    opt.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
    driver.maximize_window()
    # class variable as driver, that we can 
    # access inside class as self.driver
    request.cls.driver = driver
    yield
    driver.quit()