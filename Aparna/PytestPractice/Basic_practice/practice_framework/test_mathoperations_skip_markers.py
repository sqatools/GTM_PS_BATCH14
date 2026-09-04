import pytest

ENV="TEST" #ENV is a variable

@pytest.mark.smoke
def test_addition():
    assert 2+6==8
    
@pytest.mark.sanity
@pytest.mark.skip #unconditional skip
def test_subtraction():
    assert 4-2==2
    
@pytest.mark.sanity
@pytest.mark.regression
def test_mul():
    assert 2*6==12

@pytest.mark.regression

@pytest.mark.skipif(ENV=="PROD", reason=
                    "This feature isnot available other than test environmnet")
def test_division():
    assert 8 / 4==2
    
    