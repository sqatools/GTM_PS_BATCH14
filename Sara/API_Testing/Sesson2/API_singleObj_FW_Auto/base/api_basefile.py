'''
This file will remain the same for all the API testing sessions. 
It will contain the base URL and the endpoints for the API testing.
'''
import requests
import json
import logging

class APIBase:

    def __init__(self):
        self.log = logging.getLogger(__name__)  # to create logs for below methods with initate a constructor.

    def get_method(self,url,header_val=None,payload_val=None):
        
        headers=header_val if header_val is not None else {}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("GET", url, headers=headers, data=payload)

        res_data = response.json()
        res_status_code= response.status_code

        self.log.info(f"URL: {url}")
        self.log.info("Method = GET")
        self.log.info(f"Header : {headers}")
        self.log.info(f"Payload : {payload}")
        self.log.info(f"Response Data : {res_data}")
        self.log.info(f"Response Status Code : {res_status_code}")

        return res_data, res_status_code
    
    ##### POST METHOD #########
    def post_method(self,url,header_val=None,payload_val=None):
       
        headers=header_val if header_val is not None else {}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("POST", url, headers=headers, data=payload)

        res_data = response.json()
        res_status_code= response.status_code

        self.log.info(f"URL: {url}")
        self.log.info("Method = GET")
        self.log.info(f"Header : {headers}")
        self.log.info(f"Payload : {payload}")
        self.log.info(f"Response Data : {res_data}")
        self.log.info(f"Response Status Code : {res_status_code}")

        return res_data, res_status_code
    
    ##### PUT METHOD #########
    def put_method(self,url,header_val=None,payload_val=None):
       
        headers=header_val if header_val is not None else {}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("PUT", url, headers=headers, data=payload)

        res_data = response.json()
        res_status_code= response.status_code

        self.log.info(f"URL: {url}")
        self.log.info("Method = GET")
        self.log.info(f"Header : {headers}")
        self.log.info(f"Payload : {payload}")
        self.log.info(f"Response Data : {res_data}")
        self.log.info(f"Response Status Code : {res_status_code}")

        return res_data, res_status_code
    
    ##### DELETE METHOD #########
    def delete_method(self,url,header_val=None,payload_val=None):
       
        headers=header_val if header_val is not None else {}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        res_data = response.json()
        res_status_code= response.status_code

        self.log.info(f"URL: {url}")
        self.log.info("Method = GET")
        self.log.info(f"Header : {headers}")
        self.log.info(f"Payload : {payload}")
        self.log.info(f"Response Data : {res_data}")
        self.log.info(f"Response Status Code : {res_status_code}")

        return res_data, res_status_code
    
    ##### PATCH METHOD #########
    def patch_method(self,url,header_val=None,payload_val=None):
       
        headers=header_val if header_val is not None else {}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("PATCH", url, headers=headers, data=payload)

        res_data = response.json()
        res_status_code= response.status_code

        self.log.info(f"URL: {url}")
        self.log.info("Method = GET")
        self.log.info(f"Header : {headers}")
        self.log.info(f"Payload : {payload}")
        self.log.info(f"Response Data : {res_data}")
        self.log.info(f"Response Status Code : {res_status_code}")

        return res_data, res_status_code
        
