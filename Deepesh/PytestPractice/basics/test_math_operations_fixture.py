"""
fixture: A fixture is a function that is decorated with @pytest.fixture. 
It can be used to set up some state or data before running a test, and 
then clean up after the test is done. Fixtures can be used to provide a 
consistent and reusable way to set up test data, mock objects, or any other resources needed for testing.

@pytest.fixture(scope="function"):
def my_fixture():
    # setup code
    yield resource
    # teardown code

In this example, the fixture my_fixture is defined with a scope of "function", 
which means it will be executed for each test function that uses it. 
The setup code is executed before the test runs, and the teardown code 
is executed after the test completes. The yield statement allows you to return 
a resource that can be used in the test function.

1. function scope: The function scope is the default scope for fixtures.
This means that the fixture will be executed once for each test function that uses it.

2. class scope: The class scope means that the fixture will be executed once per test class.

3. module scope: The module scope means that the fixture will be executed once per module.

4. package scope: The package scope means that the fixture will be executed once per package.

5. session scope: The session scope means that the fixture will be executed once per execution session, 
which is typically the entire test run.

"""
import pytest

@pytest.fixture(scope="function")
def fun_fixture():
    """
    - If we want to for specific test function, then can defined as 
    parameter in the test function.

    - If we want to execute for all test function
    then we can use fixture with function scope and autouse=True

    """
    print("\n -- This is a fixture function --")
    yield 
    print("\n -- Teardown of the function fixture --")


@pytest.fixture(scope="class", autouse=True)
def class_fixture():
    print("\n -- This is a class fixture function --")
    yield 
    print("\n -- Teardown of the class fixture --")


@pytest.fixture(scope="module", autouse=True)
def module_fixture():
    print("\n -- This is a module fixture function --")
    yield 
    print("\n -- Teardown of the module fixture --")


@pytest.fixture(scope="package", autouse=True)
def package_fixture():
    print("\n -- This is a package fixture function --")
    yield 
    print("\n -- Teardown of the package fixture --")


@pytest.fixture(scope="session", autouse=True)
def session_fixture():
    print("\n -- This is a session fixture function --")
    yield 
    print("\n -- Teardown of the session fixture --")




class TestMathOperations:

    def test_addition(self):
        assert 2 + 3 == 5

    def test_subtraction(self):
        assert 5 - 2 == 3

    def test_multiplication(self, fun_fixture):
            assert 4 * 3 == 15

    def test_division(self):
        assert 10 / 2 == 5

    def test_modulus(self, fun_fixture):
        assert 10 % 3 == 1