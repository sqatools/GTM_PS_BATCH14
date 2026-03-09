from ...base.api_base import APIBase
from .restful_api_data import *

class RestFullAPI(APIBase):
    def create_new_user_with_auth_api(self):
        res, st_code = self.post_method(url=gorest_url, 
                                        header_val=auth_headers, 
                                        payload_val=new_user_payload)
        return res, st_code


