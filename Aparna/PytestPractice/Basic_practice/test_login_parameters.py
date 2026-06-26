import pytest
from database_file import db_info,user_info


@pytest.mark.parametrize("user,passwd",[('user1','pass1'),
                                        ('user2','pass2'),
                                        ('user3','pass3'),
                                        ('user4','pass4'),
                                        ('user5','pass5')])

def test_login(user,passwd):
    assert(user,passwd) in db_info 
    


@pytest.mark.parametrize("user,passwd", user_info)

def test_login_2(user,passwd):
    assert(user,passwd) in db_info
    
@pytest.mark.parametrize("name", ['Neeha','Vinod', 'Dewanssh', 'Triaksha','leo'])
def test_get_usrename(name):
    assert name in ['Neeha','Vinod','Dewanssh', 'Triaksha','Trai1']
 