'''
TO call all the 13 objects present in the below URL
https://restful-api.dev/

for the below Rest Ful API:
https://api.restful-api.dev/objects
'''
from ..base.api_basefile import APIBase  #from folder.file import classname

from .restful_testdata import *

class call_all_objects(APIBase):

    def get_all_objects(self):
        res_data, res_reason_code = self.get_method(url=pg_url) # we are getting data and reason code from the url
        return res_data, res_reason_code
    
    def get_single_object(self, id):
        new_url=f"{pg_url}/{id}"
        res_data, res_reason_code = self.get_method(url=new_url)
        return res_data, res_reason_code