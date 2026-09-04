import pytest

@pytest.mark.smoke
@pytest.mark.xfail(reason="this feature is working jira-76456")  ##expected failure
def test_addition():
    assert 2+6==5
    
@pytest.mark.sanity
@pytest.mark.xfail(reason="this feature is working jira-76456")  ##expected failure
def test_subtraction():
    assert 4-2==0
#if it is fix from the developer change the script and run the scripte 
# it shows xpasses

@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.xfail(reason="this feature is working jira-76456")

def test_mul():
    assert 2*6==12
    
@pytest.mark.sanity
def test_modulus():
    assert 10 % 3 == 1

@pytest.mark.regression
def test_division():
    assert 8 / 4==4
    
@pytest.mark.regression
def test_combined_operations():
    assert (2 + 3) * 4 - 5 / 5 == 19.0
    
    