from ..login.login_page import LoginPage
from ..login.login_testdata import LoginData


# TC13 - Long username
def test_long_username(driver):

    login = LoginPage(driver)
    login.open_login_page()

    long_user = "a" * 200

    login.enter_username(long_user)
    login.enter_password(LoginData.VALID_PASSWORD)
    login.click_login()

    assert "invalid" in login.get_error_message().lower()

# TC14 - Long password
def test_long_password(driver):

    login = LoginPage(driver)
    login.open_login_page()

    long_pass = "a" * 200

    login.enter_username(LoginData.VALID_USERNAME)
    login.enter_password(long_pass)
    login.click_login()

    assert "invalid" in login.get_error_message().lower()

# special characters in username
def test_special_character_username(driver):

    login = LoginPage(driver)
    login.open_login_page()

    login.enter_username("!@#$%^")
    login.enter_password(LoginData.VALID_PASSWORD)
    login.click_login()

    assert "invalid" in login.get_error_message().lower()

# copy paste login credentials
def test_copy_paste_login(driver):

    login = LoginPage(driver)
    login.open_login_page()

    login.enter_username(LoginData.VALID_USERNAME)
    login.enter_password(LoginData.VALID_PASSWORD)

    login.click_login()

    assert login.is_login_successful()

# refresh page after login
def test_refresh_after_login(driver):

    login = LoginPage(driver)
    login.open_login_page()

    login.login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD)

    driver.refresh()

    assert "secure" in driver.current_url


# direct access to secure page without login
def test_direct_secure_access(driver):

    login = LoginPage(driver)

    login.open_secure_page()

    assert "login" in driver.current_url

# session after logout
def test_session_after_logout(driver):

    login = LoginPage(driver)
    login.open_login_page()

    login.login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD)

    login.logout()

    driver.back()

    assert "login" in driver.current_url