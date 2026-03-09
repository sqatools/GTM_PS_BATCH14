from ...base.api_base import APIBase
from .restful_api_data import *

class RestFullAPI(APIBase):

    def create_new_object(self):
        res, st_code = self.post_method(url=common_url, 
                                        header_val=new_object_headers, 
                                        payload_val=create_new_object_payload)
        return res, st_code
    
    def delete_new_object(self):
        res, st_code = self.post_method(url=common_url, 
                                        header_val=new_object_headers, 
                                        payload_val=create_new_object_payload2)
        new_id = res["id"]
        new_url = f"{common_url}/{new_id}"
        delete_res, st_code = self.delete_method(url=new_url)
        return delete_res, st_code