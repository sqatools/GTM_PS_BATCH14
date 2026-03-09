import pytest
from ..api_objects.restful_api.restful_api_class import RestFullAPI
from ..api_objects.restful_api.restful_api_data import *


class TestRestfulAPI:
    @pytest.fixture(scope = "function", autouse = True)
    def setup(self):
        self.rp = RestFullAPI()

    def test_create_new_and_verify(self):
        response, st_code = self.rp.create_new_user_with_auth_api()
        assert st_code == 201
        assert "id" in response
        assert response["name"] == "Sohan Kumar Ramakrishna"
    
    