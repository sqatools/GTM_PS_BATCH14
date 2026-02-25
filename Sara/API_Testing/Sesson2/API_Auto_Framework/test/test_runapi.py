import pytest
from ..page_objects.api_restful_class import call_all_objects

class run_api_scenario():

    @pytest.fixture(scope="function", autouse=True)
    def setup_restful_class(self):
        self.RP = call_all_objects() # careating object of another/inheritate class

     # to call all the methods present in above class   
    def test_get_objects_method(self):
            res_data, status_reason_code = self.RP.get_all_objects() # get_all_object is the method name in restful class file
   

            assert len(res_data)==13
            assert status_reason_code == 200

       

