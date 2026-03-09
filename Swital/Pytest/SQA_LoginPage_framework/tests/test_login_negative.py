from ..login.login_page import LoginPage
from ..login.login_testdata import LoginData


# TC09 Invalid username
def test_invalid_username(driver):

    login = LoginPage(driver)
    login.open_login_page()

    login.enter_username("wrongUser")
    login.enter_password("SuperSecretPassword!")
    login.click_login()

    message = login.get_error_message()

    assert "invalid" in message.lower()

# TC10 Invalid password
def test_invalid_password(driver):

    login = LoginPage(driver)
    login.open_login_page()

    login.enter_username("practice")
    login.enter_password("wrongPassword")
    login.click_login()

    message = login.get_error_message()

    assert "invalid" in message.lower()

# TC11 Both username and password invalid
def test_both_invalid(driver):

    login = LoginPage(driver)
    login.open_login_page()

    login.enter_username("wrongUser")
    login.enter_password("wrongPassword")
    login.click_login()

    message = login.get_error_message()

    assert "invalid" in message.lower()

# TC12 Empty username 
def test_empty_username(driver):

    login = LoginPage(driver)
    login.open_login_page()

    login.enter_username("")
    login.enter_password("SuperSecretPassword!")
    login.click_login()

    message = login.get_error_message()

    assert "invalid" in message.lower()

# TC13 Empty password
def test_empty_password(driver):

    login = LoginPage(driver)
    login.open_login_page()

    login.enter_username("practice")
    login.enter_password("")
    login.click_login()

    message = login.get_error_message()

    assert "invalid" in message.lower()

# TC14 Empty username and password
def test_both_empty(driver):

    login = LoginPage(driver)
    login.open_login_page()

    login.enter_username("")
    login.enter_password("")
    login.click_login()

    message = login.get_error_message()

    assert "invalid" in message.lower()

# SQL Injection test
def test_sql_injection(driver):

    login = LoginPage(driver)
    login.open_login_page()

    login.enter_username("' OR '1'='1")
    login.enter_password("' OR '1'='1")
    login.click_login()

    message = login.get_error_message()

    assert "invalid" in message.lower()

# Script Injection test
def test_script_injection(driver):

    login = LoginPage(driver)
    login.open_login_page()

    login.enter_username("<script>alert()</script>")
    login.enter_password("password")
    login.click_login()

    message = login.get_error_message()

    assert "invalid" in message.lower()