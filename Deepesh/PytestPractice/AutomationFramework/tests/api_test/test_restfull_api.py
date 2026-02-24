import pytest
from ...api_objects.restfull_api.resfull_api_class import RestFullAPI
from ...api_objects.restfull_api.restfull_api_data import *

class TestResfullAPI:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.rp = RestFullAPI()


    def test_get_all_objects_verify(self):
        response, st_code = self.rp.get_all_objects()
        assert len(response) == 13
        assert st_code == 200


    def test_specific_id_details_and_verify(self):
        response, st_code = self.rp.get_specific_object_details(single_obj_id)
        assert len(response) == 3
        assert response["id"] == single_obj_id
        assert st_code == 200

        response, st_code = self.rp.get_specific_object_details(single_obj_id2)
        assert len(response) == 3
        assert response["id"] == single_obj_id2
        assert st_code == 200