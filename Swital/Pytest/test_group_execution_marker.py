import pytest

@pytest.mark.smoke
def test_smoke_login_UN():
    print("smoke login case login")

@pytest.mark.smoke
def test_smoke_login_PWD():
    print("smoke login case password")

@pytest.mark.smoke
def test_smoke_login_btn():
    print("login successfully")

@pytest.mark.sanity
def test_dashboard_table():
    print("Print table")

@pytest.mark.sanity
def test_dashboard_chart():
    print("chart check")

@pytest.mark.smoke
@pytest.mark.paymenttest
def test_payment_feature():
    print("check the payment")

@pytest.mark.sanity
@pytest.mark.paymenttest
def test_pay_feature():
    print("payment done")
