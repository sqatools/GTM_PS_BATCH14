"""
pytest fixture: Fixture is a function that runs before each 
test function to set up any necessary preconditions or state. 
It can be used to create test data, initialize resources, or 
perform any setup tasks required for the tests.

To execute a fixture function: python -m pytest -v -s .\filename.py

-s : to execute the text mentioned before and after the yield statement in the fixture function.

"""

import pytest

@pytest.fixture(scope="function", autouse=True)
def fun_fixture():
    print("\n -- This is a fixture function --")
    yield 
    print("\n -- Teardown of the function fixture --")

class TestMathOperations:

    def test_addition(self, fun_fixture):
        assert 2 + 3 == 5

    def test_subtraction(self):
        assert 5 - 2 == 3

    def test_multiplication(self):
            assert 4 * 3 == 12

    def test_division(self):
        assert 10 / 2 == 5

    def test_modulus(self):
        assert 10 % 3 == 1