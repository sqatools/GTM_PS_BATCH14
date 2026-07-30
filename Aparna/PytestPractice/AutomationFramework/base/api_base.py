import logging

import requests


class APIBase:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    #def _parse_response(self, response):
      #  try:
      #      return response.json(), response.status_code
      #  except ValueError:
      #      return {"raw_response": response.text, "status_code": response.status_code}, response.status_code

    def get_method(self, url, header_val=None, payload_val=None):
        headers = header_val if header_val is not None else {}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("GET", url, headers=headers, data=payload, timeout=10)
        res_data = response.json()
        st_code = response.status_code
        self.logger.info(f"url : {url}")
        self.logger.info("Method Name : GET")
        self.logger.info(f"Headers : {headers}")
        self.logger.info(f"Headers : {headers}")
        self.logger.info(f"payload : {payload}")
        self.logger.info(f"reponse : {res_data}")
        self.logger.info(f"status code : {st_code}")
        return res_data, st_code

    def post_method(self, url, headers_val=None, payload_val=None):
        headers = headers_val if headers_val is not None else {}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("POST", url, headers=headers, data=payload, timeout=10)
        #res_data, st_code = self._parse_response(response)
        res_data = response.json()
        st_code = response.status_code
        self.logger.info(f"url : {url}")
        self.logger.info("Method Name : POST")
        self.logger.info(f"Headers : {headers}")
        self.logger.info(f"Headers : {headers}")
        self.logger.info(f"payload : {payload}")
        self.logger.info(f"reponse : {res_data}")
        self.logger.info(f"status code : {st_code}")
        return res_data, st_code

    def put_method(self, url, headers_val=None, payload_val=None):
        headers = headers_val if headers_val is not None else {}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("PUT", url, headers=headers, data=payload, timeout=10)
        #res_data, st_code = self._parse_response(response)
        res_data = response.json()
        st_code = response.status_code
        self.logger.info(f"url : {url}")
        self.logger.info("Method Name : PUT")
        self.logger.info(f"Headers : {headers}")
        self.logger.info(f"Headers : {headers}")
        self.logger.info(f"payload : {payload}")
        self.logger.info(f"reponse : {res_data}")
        self.logger.info(f"status code : {st_code}")
        return res_data, st_code

    def patch_method(self, url, headers_val=None, payload_val=None):
        headers = headers_val if headers_val is not None else {}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("PATCH", url, headers=headers, data=payload, timeout=10)
        #res_data, st_code = self._parse_response(response)
        res_data = response.json()
        st_code = response.status_code
        self.logger.info(f"url : {url}")
        self.logger.info("Method Name : PATCH")
        self.logger.info(f"Headers : {headers}")
        self.logger.info(f"Headers : {headers}")
        self.logger.info(f"payload : {payload}")
        self.logger.info(f"reponse : {res_data}")
        self.logger.info(f"status code : {st_code}")
        return res_data, st_code

    def delete_method(self, url, headers_val=None, payload_val=None):
        headers = headers_val if headers_val is not None else {}
        payload = payload_val if payload_val is not None else {}

        response = requests.request("DELETE", url, headers=headers, data=payload, timeout=10)
        #res_data, st_code = self._parse_response(response)
        res_data = response.json()
        st_code = response.status_code
        self.logger.info(f"url : {url}")
        self.logger.info("Method Name : DELETE")
        self.logger.info(f"Headers : {headers}")
        self.logger.info(f"Headers : {headers}")
        self.logger.info(f"payload : {payload}")
        self.logger.info(f"reponse : {res_data}")
        self.logger.info(f"status code : {st_code}")
        return res_data, st_code


APIBASE = APIBase

