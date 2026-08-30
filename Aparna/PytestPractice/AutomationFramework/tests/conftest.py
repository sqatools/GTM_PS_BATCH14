#drivers
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

#fixture to get the driver instance and provide it to the test class
@pytest.fixture(scope="class")
def get_driver(request):
    opt = Options()
    #no needto lsnch browser
    opt.add_argument = ('--headless')
    driver = webdriver.Chrome()
    driver.maximize_window()
    #class variable as driver that can be accessed in the test class as self.driver
    request.cls.driver = driver
    yield driver
    driver.quit()