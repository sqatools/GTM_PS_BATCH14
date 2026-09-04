import requests
import json
import logging

class APIBase:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def get_method(self, url, headers_val=None, payload_val=None):
        headers = headers_val if headers_val is not None else {}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("GET", url, headers=headers, data=payload)
        res_data = response.json()
        st_code = response.status_code
        self.log.info(f"url : {url}")
        self.log.info("Method Name : GET")
        self.log.info(f"Headers : {headers}")
        self.log.info(f"payload : {payload}")
        self.log.info(f"reponse : {res_data}")
        self.log.info(f"status code : {st_code}")
        return res_data, st_code
    

    def post_method(self, url, headers_val=None, payload_val=None):
        headers = headers_val if headers_val is not None else {}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("POST", url, headers=headers, data=payload)
        res_data = response.json()
        st_code = response.status_code
        self.log.info(f"url : {url}")
        self.log.info("Method Name : POST")
        self.log.info(f"Headers : {headers}")
        self.log.info(f"Headers : {headers}")
        self.log.info(f"payload : {payload}")
        self.log.info(f"reponse : {res_data}")
        self.log.info(f"status code : {st_code}")
        return res_data, st_code
    

    def put_method(self, url, headers_val=None, payload_val=None):
        headers = headers_val if headers_val is not None else {}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("PUT", url, headers=headers, data=payload)
        res_data = response.json()
        st_code = response.status_code
        self.log.info(f"url : {url}")
        self.log.info("Method Name : PUT")
        self.log.info(f"Headers : {headers}")
        self.log.info(f"Headers : {headers}")
        self.log.info(f"payload : {payload}")
        self.log.info(f"reponse : {res_data}")
        self.log.info(f"status code : {st_code}")
        return res_data, st_code
    
    def patch_method(self, url, headers_val=None, payload_val=None):
        headers = headers_val if headers_val is not None else {}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("PATCH", url, headers=headers, data=payload)
        res_data = response.json()
        st_code = response.status_code
        self.log.info(f"url : {url}")
        self.log.info("Method Name : PATCH")
        self.log.info(f"Headers : {headers}")
        self.log.info(f"Headers : {headers}")
        self.log.info(f"payload : {payload}")
        self.log.info(f"reponse : {res_data}")
        self.log.info(f"status code : {st_code}")
        return res_data, st_code
    
    def delete_method(self, url, headers_val=None, payload_val=None):
        headers = headers_val if headers_val is not None else {}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("DELETE", url, headers=headers, data=payload)
        res_data = response.json()
        st_code = response.status_code
        self.log.info(f"url : {url}")
        self.log.info("Method Name : DELETE")
        self.log.info(f"Headers : {headers}")
        self.log.info(f"Headers : {headers}")
        self.log.info(f"payload : {payload}")
        self.log.info(f"reponse : {res_data}")
        self.log.info(f"status code : {st_code}")
        return res_data, st_code
    




