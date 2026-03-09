## ***** Math Operation Marker Fail ********


import pytest

@pytest.mark.smoke
@pytest.mark.xfail(reason="This feature is working JIRA-36634")
def test_addition():
    assert 2 + 3 == 8

@pytest.mark.smoke
#@pytest.mark.xfail(reason="This feature is working JIRA-36876")
def test_subtraction():
    assert 5 - 2 == 3

@pytest.mark.smoke
def test_multiplication():
    assert 4 * 3 == 15

@pytest.mark.smoke
@pytest.mark.sanity
def test_division():
    assert 10 / 2 == 5

@pytest.mark.sanity
def test_modulus():
    assert 10 % 3 == 1

@pytest.mark.sanity
def test_exponentiation():
    assert 2 ** 3 == 8

@pytest.mark.regression
def test_floor_division():
    assert 10 // 3 == 3

@pytest.mark.regression
def test_combined_operations():
    assert (2 + 3) * 4 - 5 / 5 == 19.0