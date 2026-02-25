import pytest
from ..page_objects.api_restful_class import call_all_objects
from ..page_objects.restful_testdata import *

class run_api_scenario():

    @pytest.fixture(scope="function", autouse=True)
    def setup_restful_class(self):
        self.RP = call_all_objects() # careating object of another/inheritate class

     # to call all the methods present in above class   
    def test_get_objects_method(self):
            res_data, status_reason_code = self.RP.get_all_objects() # get_all_object is the method name in restful class file
   

            assert len(res_data)==13
            assert status_reason_code == 200

    def test_specfic_id(self):
         res_data, status_reason_code = self.RP.get_single_object(single_object)        
         
         assert len(res_data)== 3
         assert res_data ['id'] == single_object
         assert status_reason_code == 200

