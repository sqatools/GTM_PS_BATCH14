import requests
import json


def get_all_objects():
    url = "https://api.restful-api.dev/objects"
    payloads = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data = payloads)
    print("Status code:", response.status_code)
    print("Resonse in json format:", response.json())
    assert len(response.json()) ==13, "Numbers of objects returned are more than expected"
    assert response.json()[-1]['id'] == "13"
    assert response.json()[-1]['name'] == "Apple iPad Air"

#get_all_objects()

print("#"*100)

def get_specific_id():
    url = "https://api.restful-api.dev/objects/7"
    payloads = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data = payloads)
    print("Status code:", response.status_code)
    print("Resonse in json format:", response.json())

#get_specific_id()

def add_new_object():

    url = "https://api.restful-api.dev/objects"

    payload = json.dumps({
    "id": "9",
    "name": "Beats Studio3 Wireless",
    "data": {
        "Color": "Red",
        "Description": "High-performance wireless noise cancelling headphones"
    }
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)
    print(response.json())

add_new_object()
