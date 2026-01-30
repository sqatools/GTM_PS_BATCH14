import pytest

@pytest.mark.smoke
def test_addition():
    assert 2 + 3 == 5   

@pytest.mark.smoke
def test_subtraction():
    assert 5 - 2 == 3   

@pytest.mark.sanity
@pytest.mark.smoke
def test_multiplication():
    assert 4 * 3 == 12  

@pytest.mark.regression
def test_division():
    assert 10 / 2 == 15

@pytest.mark.regression
def test_modulus():
    assert 10 % 3 == 1

@pytest.mark.sanity
def test_exponentiation():
    assert 2 ** 3 == 8

def test_floor_division():
    assert 10 // 3 == 3