from ...base.api_base import APIBase
from .restful_api_data import *

class RestFullAPI(APIBase):

    def get_all_objects(self):
        res, st_code = self.get_method(url = common_url)
        return res, st_code
    
    def get_specific_object_detailS(self, id):
        new_url = f"{common_url}/{id}"
        res, st_code = self.get_method(url = new_url)
        return res, st_code
    
    def create_new_object(self):
        res, st_code = self.post_method(url=common_url, 
                                        header_val=new_object_headers, 
                                        payload_val=create_new_object_payload)
        return res, st_code