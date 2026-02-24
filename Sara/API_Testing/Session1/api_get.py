import requests
import json

def get_objects():
    url = "https://api.restful-api.dev/objects"
    payload = {} 
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print("Status code:", response.status_code)
    print("Status Response text:", response.json())
    assert len(response.json()) == 13, "NUmber objects received are not as per the expectation"
    #assert response.json()[-1]['id'] == "13"
    #assert response.json()[-1]['name'] == "Apple iPad Air"

#get_objects()

########################## Get by ID ##########################

def get_object_by_id():
    url="https://api.restful-api.dev/objects/7" # since we gae /7 it means we are looking for a specfic object

    payload = {}
    headers = {}

    response = requests.request("GET",url, headers=headers, data=payload)

    print("Status code:", response.status_code)
    print("Status Response text:", response.json())

get_object_by_id()

"""
Status code: 200
Status Response text: {'id': '7', 'name': 'Apple MacBook Pro 16', 'data': {'year': 2019, 'price': 1849.99, 'CPU model': 'Intel Core i9', 'Hard disk size': '1 TB'}}

"""
