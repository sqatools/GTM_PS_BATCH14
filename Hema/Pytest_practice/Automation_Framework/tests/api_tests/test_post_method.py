import pytest
from api_objects.restful_api.restful_api_class import RestfulAPI
from api_objects.restful_api.restful_api_data import *

class TestPostMethod:
    @pytest.fixture(scope="function", autouse= True)
    def setup(self):
        self.apitest2 = RestfulAPI()

    def test_post_method_for_objects_And_verify(self):
        response, statuscode = self.apitest2.post_method_for_objects(payload=data_for_post_method)
        assert response["name"] == data_for_post_method["name"]
#         assert response["data"] == data_for_post_method["{
#     "year": 2025,
#     "price": 2000.00,
#     "CPU model": "Intel Core i9",
#     "Hard disk size": "2 TB"
#   }"]
        assert statuscode == 201

