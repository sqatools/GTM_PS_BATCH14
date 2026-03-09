from ..login.login_page import LoginPage
from ..login.login_testdata import LoginData

# TC01 - Successful login
def test_successful_login(driver):

    login = LoginPage(driver)

    login.open_login_page()

    login.login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD)

    assert login.is_login_successful()

# TC02 - Login then logout
def test_login_then_logout(driver):

    login = LoginPage(driver)

    login.open_login_page()

    login.login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD)

    assert "secure" in driver.current_url

    login.logout()

    assert "login" in driver.current_url


# TC03 - Login again after logout
def test_login_again_after_logout(driver):

    login = LoginPage(driver)

    login.open_login_page()

    login.login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD)

    login.logout()

    login.login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD)

    assert "secure" in driver.current_url


# TC04 - Login after refreshing page
def test_login_after_refresh(driver):

    login = LoginPage(driver)

    login.open_login_page()

    login.refresh_page()

    login.login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD)

    assert login.is_login_successful()


# TC05 - Login after clearing fields
def test_login_after_clearing_fields(driver):

    login = LoginPage(driver)

    login.open_login_page()

    login.enter_username(LoginData.VALID_USERNAME)
    login.enter_password(LoginData.VALID_PASSWORD)

    login.clear_username()
    login.clear_password()

    login.login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD)

    assert login.is_login_successful()


# TC06 - Login using keyboard enter
def test_login_using_enter_key(driver):

    login = LoginPage(driver)

    login.open_login_page()

    login.login_with_enter(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD)

    assert login.is_login_successful()

# TC07 - Login after page reload
def test_login_after_reload(driver):

    login = LoginPage(driver)

    login.open_login_page()

    login.enter_username(LoginData.VALID_USERNAME)
    login.enter_password(LoginData.VALID_PASSWORD)

    login.refresh_page()

    login.login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD)

    assert login.is_login_successful()

# TC08 - Multiple successful login attempts
def test_multiple_login_attempts(driver):

    login = LoginPage(driver)

    login.open_login_page()

    login.login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD)

    login.logout()

    login.login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD)

    login.logout()