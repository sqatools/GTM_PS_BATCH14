import pytest
from ..api_objects.restful_api.restful_api_class import RestFullAPI
from ..api_objects.restful_api.restful_api_data import *


class TestRestfulAPI:
    @pytest.fixture(scope = "function", autouse = True)
    def setup(self):
        self.rp = RestFullAPI()

    def test_get_all_objects_verify(self):
        response, st_code = self.rp.get_all_objects()
        assert len(response) == 13
        assert st_code == 200
    
    def test_create_new_object_and_verify(self):
        response, st_code = self.rp.create_new_object()
        assert "id" in response
        assert response['name'] == "Apple MacBook Pro 16"
        assert response['data']['year'] == 2019
        assert st_code == 200