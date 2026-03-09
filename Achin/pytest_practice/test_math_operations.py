
def test_addition():
    assert 2 + 3 == 5

def test_subtraction():
    assert 5 - 2 == 3

def test_multiplication():
    assert 4 * 3 == 12

def test_division():
    assert 10 / 2 == 5

def test_modulus():
    assert 10 % 3 == 1

#for running the tests, use the command:
# python -m pytest -v .\test_math_operations.py