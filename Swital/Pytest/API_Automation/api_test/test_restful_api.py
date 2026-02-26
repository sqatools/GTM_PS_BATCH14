import pytest
from ..api_objects.restful_api.restful_api_class import RestFullAPI

class TestRestfulAPI:
    @pytest.fixture(scope = "function", autouse = True)
    def setup(self):
        self.rp = RestFullAPI()

    def test_get_all_objects_verify(self):
        response, st_code = self.rp.get_all_objects()
        assert len(response) == 13
        assert st_code == 200