

import pytest

from ...api_objects.restfull_api.resfull_api_class import RestFullAPI
from ...api_objects.restfull_api.resfull_api_class import single_obj_id
from ...api_objects.restfull_api.resfull_api_class import single_obj_id2


class TestRestFullAPI:
    @pytest.fixture(scope="function",autouse=True)
    def setup(self):
        self.rp = RestFullAPI()

    # @pytest.mark.api
    # def test_get_all_objects_verify(self):
    #     response, st_code = self.rp.get_all_objects()
    #     assert st_code in (200, 403)
    #     if st_code == 200:
    #         assert isinstance(response, list)
    #         assert len(response) >= 1
    #     else:
    #         assert "raw_response" in response
    #         assert "API key is missing" in response["raw_response"]

    # @pytest.mark.api
    # def test_specific_id_details_and_verify(self):
    #     response, st_code = self.rp.get_specific_object_details(single_obj_id)
    #     assert st_code in (200, 403)
    #     if st_code == 200:
    #         assert response["id"] == single_obj_id
    #     else:
    #         assert "raw_response" in response
    #         assert "API key is missing" in response["raw_response"]

    #     response, st_code = self.rp.get_specific_object_details(single_obj_id2)
    #     assert st_code in (200, 403)
    #     if st_code == 200:
    #         assert response["id"] == single_obj_id2
    #     else:
    #         assert "raw_response" in response
    #         assert "API key is missing" in response["raw_response"]

    # @pytest.mark.api
    # def test_create_new_object_and_verify(self):
    #     response, st_code = self.rp.create_new_object()
    #     assert st_code in (200, 403)
    #     if st_code == 200:
    #         assert "id" in response
    #         assert response["name"] == "Apple MacBook Pro 16"
    #         assert response["data"]["year"] == 2019
    #     else:
    #         assert "raw_response" in response
    #         assert "API key is missing" in response["raw_response"]

    # @pytest.mark.api
    # def test_delete_object_and_verify(self):
    #     response, st_code = self.rp.delete_new_object()
    #     assert st_code == 200 or st_code == 201
    #     assert st_code == 200 or st_code == 201
    #     assert "has been deleted" in response["message"]
    #     #assert "id" in response

    #     #new_id = response["id"]
    #     #assert st_code in (200, 403)
    #     #if st_code == 200:
    #      #   assert "has been deleted" in response["message"]
    #     #else:
    #       #  assert "raw_response" in response
    #        # assert "API key is missing" in response["raw_response"]

    # @pytest.mark.api
    # def test_create_new_and_verify(self):
    #     response, st_code = self.rp.create_new_user_with_auth_api()
    #     assert st_code in (201, 403)
    #     if st_code == 201:
    #         assert "id" in response
    #         assert response["name"] == "Dews"
    #     else:
    #         assert "raw_response" in response
    #         assert "API key is missing" in response["raw_response"]
    
    @pytest.mark.api
    def test_get_all_objects_verify(self):
            response, st_code = self.rp.get_all_objects()
            assert len(response) == 13
            assert st_code == 200
            
    @pytest.mark.api
    def test_specific_id_details_and_verify(self):
            response, st_code = self.rp.get_specific_object_details(single_obj_id)
            assert len(response) == 3
            assert response["id"] == single_obj_id
            assert st_code == 200
    
            response, st_code = self.rp.get_specific_object_details(single_obj_id2)
            assert len(response) == 3
            assert response["id"] == single_obj_id2
            assert st_code == 200
    
    @pytest.mark.api
    def test_create_new_object_and_verify(self):
            response, st_code = self.rp.create_new_object()
            assert "id" in response
            assert response['name'] == "Apple MacBook Pro 16"
            assert response['data']['year'] == 2019
            assert st_code == 200
    
    @pytest.mark.api
    def test_delete_object_and_verify(self):
            response, st_code = self.rp.delete_new_object()
            assert st_code == 200
            assert "has been deleted" in response["message"]
    
    @pytest.mark.api
    def test_create_new_and_verify(self):
            response, st_code = self.rp.create_new_user_with_auth_api()
            assert st_code == 201
            assert "id" in response
            assert response["name"] == "Hello API"
    
    