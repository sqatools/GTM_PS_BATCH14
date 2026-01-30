"""
Program 1

def test_addition():
    10+20 == 30

def test_subtraction():
    20-10 == 10

def test_multiplication():
    5*5 == 25
    
    def test_division():
        20/5 == 4

"""
#Program 2: Markers applied

import pytest


@pytest.mark.priority1
def test_addition():
    assert 10+20 == 30

@pytest.mark.priority2
def test_subtraction():
    assert 20-10 == 10

@pytest.mark.priority2
def test_multiplication():
        assert 5*5 == 25

@pytest.mark.priority1
def test_division():
        assert 20/5 == 4

@pytest.mark.priority1
@pytest.mark.priority2
def test_multiplication():
    assert 4 * 3 == 12

""""
python -m pytest -v -m "priority1" .\test_Session1.py

test_Session1.py::test_addition PASSED                                    [ 33%] 
test_Session1.py::test_multiplication PASSED                              [ 66%] 
test_Session1.py::test_division PASSED

"""




