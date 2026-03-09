from api_objects.restful_api.restful_api_data import *
from base.api_base import APIBase

class RestfulAPI(APIBase):
    def get_all_objects(self):
        res, sts_code = self.get_method(url=common_url)
        return res, sts_code

    def get_specific_object_details(self, id):
        #new_url = common_url/id
        new_url = f"{common_url}/{id}"
        res, sts_code = self.get_method(url=new_url)
        return res, sts_code
    
    def post_method_for_objects(self, payload):
        payload = data_for_post_method
        res, sts_code = self.post_method(url=common_url, payload_val=payload)
        return res, sts_code
