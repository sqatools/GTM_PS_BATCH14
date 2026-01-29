import pytest

@pytest.mark.smoke
def test_addition():
    assert 2 + 3 == 5
    
@pytest.mark.regression
def test_subtraction():
    assert 5 - 2 == 3

@pytest.mark.sanity
def test_multiplication():
    assert 4 * 3 == 15

@pytest.mark.performance
def test_division():
    assert 10 / 2 == 5

@pytest.mark.sanity
def test_modulus():
    assert 10 % 3 == 1