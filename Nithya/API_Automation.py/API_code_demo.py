import requests
import json
#pip install requests
"""
def get_all_objects():

    url = "https://api.restful-api.dev/objects"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print("Get status code:", response.text)
    print("Get response body:", response.json())

get_all_objects()
"""
# Adding a new object:

def add_new_object():

    url = "https://api.restful-api.dev/collections/objects"

    payload = json.dumps({
    "name": "Apple MacBook Pro 16",
     "data": {
    "year": 2019,
    "price": 1849.99,
    "CPU model": "Intel Core i9",
    "Hard disk size": "1 TB"
    }
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print("Get status code:", response.status_code)
    print("Get response body:", response.text)

add_new_object()