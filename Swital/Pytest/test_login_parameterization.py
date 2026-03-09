import pytest
from db_login_data import data_info

@pytest.mark.parametrize("user, passwd", [
    ('user1', 'pwd1'), 
    ('user2', 'pwd2'), 
    ('user5', 'pwd5')
])
def test_login(user, passwd):
    assert(user, passwd) in data_info