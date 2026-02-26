import logging
import json
import requests


class APIBase:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def get_method(self, url, headers_val= None, payload_val = None):
        headers = headers_val if headers_val is not None else {}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("GET", url, headers=headers, json=payload)
        response_data = response.json()
        status_code_number = response.status_code

        self.log.info(f"url : {url}")
        self.log.info(f"Method name : GET")
        self.log.info(f"headers : {headers}")
        self.log.info(f"payload: {payload}")
        self.log.info(f"response : {response_data}")
        self.log.info(f"status code : {status_code_number}")

        return response_data, status_code_number
    
    def post_method(self, url, headers_val= None, payload_val = None ):
        headers = headers_val if headers_val is not None else { "Content-Type": "application/json"}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("POST", url, headers=headers, data=payload)
        response_data = response.json()
        status_code_number = response.status_code

        self.log.info(f"url : {url}")
        self.log.info(f"Method name : POST")
        self.log.info(f"headers : {headers}")
        self.log.info(f"payload: {payload}")
        self.log.info(f"response : {response_data}")
        self.log.info(f"status code : {status_code_number}")

        return response_data, status_code_number

    def put_method(self, url, headers_val= None, payload_val = None ):
        headers = headers_val if headers_val is not None else { "Content-Type": "application/json"}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("PUT", url, headers=headers, data=payload)
        response_data = response.json()
        status_code_number = response.status_code

        self.log.info(f"url : {url}")
        self.log.info(f"Method name : PUT")
        self.log.info(f"headers : {headers}")
        self.log.info(f"payload: {payload}")
        self.log.info(f"response : {response_data}")
        self.log.info(f"status code : {status_code_number}")

        return response_data, status_code_number
    
    def patch_method(self, url, headers_val= None, payload_val = None ):
        headers = headers_val if headers_val is not None else {}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("PATCH", url, headers=headers, data=payload)
        response_data = response.json()
        status_code_number = response.status_code

        self.log.info(f"url : {url}")
        self.log.info(f"Method name : PATCH")
        self.log.info(f"headers : {headers}")
        self.log.info(f"payload: {payload}")
        self.log.info(f"response : {response_data}")
        self.log.info(f"status code : {status_code_number}")

        return response_data, status_code_number
    
    def delete_method(self, url, headers_val= None, payload_val = None ):
        headers = headers_val if headers_val is not None else {}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("DELETE", url, headers=headers, data=payload)
        response_data = response.json()
        status_code_number = response.status_code

        self.log.info(f"url : {url}")
        self.log.info(f"Method name : DELETE")
        self.log.info(f"headers : {headers}")
        self.log.info(f"payload: {payload}")
        self.log.info(f"response : {response_data}")
        self.log.info(f"status code : {status_code_number}")

        return response_data, status_code_number
    