import pytest
from api_objects.restful_api.restful_api_class import RestfulAPI
from api_objects.restful_api.restful_api_data import *

class Test_restful_api:
    @pytest.fixture(scope="function", autouse= True)
    def setup(self):
        self.apitest1 = RestfulAPI()

    def test_getallobjects_And_verify(self):
        response, statuscode = self.apitest1.get_all_objects()
        assert len(response) == 13
        assert statuscode == 200

    def test_get_specificobjectdetails_And_verify(self):
        response, statuscode = self.apitest1.get_specific_object_details(single_obj_id)
        assert len(response) == 3
        assert response["id"] == single_obj_id
        assert statuscode == 200

        

