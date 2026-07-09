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
e.g,

"""
import pytest
#Fresh browser for every test
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

#e.g Execute all tests in one page/module after login
@pytest.fixture(scope="class", autouse=True)
def class_fixture():
    print("\n -- This is a class fixture function --")
    yield 
    print("\n -- Teardown of the class fixture --")

#Share browser across one test file
@pytest.fixture(scope="module", autouse=True)
def module_fixture():
    print("\n -- This is a module fixture function --")
    yield 
    print("\n -- Teardown of the module fixture --")


#Share setup across multiple files in same package
@pytest.fixture(scope="package", autouse=True)
def package_fixture():
    print("\n -- This is a package fixture function --")
    yield 
    print("\n -- Teardown of the package fixture --")

#total application will take,Initialize browser/database once for entire suite
@pytest.fixture(scope="session", autouse=True)
def session_fixture():
    print("\n -- This is a session fixture function --")
    yield 
    print("\n -- Teardown of the session fixture --")


#without self the class cannot create function in a class
#when we create aclass it should start with test

class TestMathOperations:

    def test_addition(self):
        assert 2 + 3 == 5

    def test_subtraction(self):
        assert 5 - 2 == 3
#for specific function not for all
    def test_multiplication(self, fun_fixture):
            assert 4 * 3 == 15

    def test_division(self):
        assert 10 / 2 == 5

    def test_modulus(self, fun_fixture):
        assert 10 % 3 == 1
        
        
        """1.Open a fresh browser for every test.
        test_login
    Open Chrome
    Execute Test
    Close Chrome

test_logout
    Open Chrome
    Execute Test
    Close Chrome
    2.Login once and execute multiple related tests.
    Open Chrome

test_profile
test_settings
test_logout

Close Chrome
3.Run all tests in one file using the same browser.
Open Chrome

test_users
test_roles
test_permissions

Close Chrome
4.share setup across multiple test files in the same package
tests/
│
├── admin/
│   ├── test_users.py
│   ├── test_roles.py
│   └── conftest.py
5.Open browser once for the entire automation suite.


#------Execution structure fixture-------33e   
start session  fixture
    package fixture
        modules fixture
            class fixture
                function fixture start
                test
                function fixture  teardown
            class fixture teardown
        module fixture teardown
    packae fixture teardown
session fixture  teardown


        """