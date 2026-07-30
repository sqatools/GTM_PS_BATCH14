

from ...base.api_base import APIBase
from .restfull_api_data import (
    common_url,
    new_object_headers,
    create_new_object_payload,
    create_new_object_payload2,
    auth_headers,
    new_user_payload,
    gorest_url,
    single_obj_id,
    single_obj_id2,
)

class RestFullAPI(APIBase):

    def get_all_objects(self):
        res, st_code = self.get_method(url=common_url)
        return res, st_code


    def get_specific_object_details(self, id):
        new_url = f"{common_url}/{id}"
        res, st_code = self.get_method(url=new_url)
        return res, st_code


    def create_new_object(self):
        
        res, st_code = self.post_method(url=common_url, 
                                        headers_val=new_object_headers, 
                             payload_val=create_new_object_payload)
        return res, st_code
    
    def delete_new_object(self):
        res, st_code = self.post_method(url=common_url, 
                                        headers_val=new_object_headers, 
                                        payload_val=create_new_object_payload2)
        new_id = res["id"]
        new_url = f"{common_url}/{new_id}"
        delete_res, st_code = self.delete_method(url=new_url)
        return delete_res, st_code
    
    def create_new_user_with_auth_api(self):
        res, st_code = self.post_method(url=gorest_url, 
                                        headers_val=auth_headers, 
                                        payload_val=new_user_payload)
        return res, st_code


