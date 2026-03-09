"""
API :  Application Programming Interface

PRESENTATION LAYER
     |
Business Layer (API)
     |
Database Layer

1. Free API : Everyone access it.
2. Private API : Specific Organasation
3. Paid API : Businesses has to pay subscription fee to access API service.

HTTP Method
1. GET : get existing information
2. POST : Add new entry entry.
3. PUT : Add new entry and update existing entry.
4. PATCH : Update specific field of existing entry
5. DELETE : Delete entry

API Status Code :
100-199 : Informational status code
200-299 : Success code
300-399 :  Redirectional code
400-499 : Client Error
500-599 : Server Error
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status#information_responses

"""
# requests method help to execute all https methods and return response
import requests
# pip install requests
import json

def get_all_objects():
    url = "https://api.restful-api.dev/objects"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print("status code :", response.status_code)
    print("status reponse :", response.json())
    assert len(response.json()) == 13, "NUmber objects received are not as per the expectation"
    assert response.json()[-1]['id'] == "13"
    assert response.json()[-1]['name'] == "Apple iPad Air"

#get_all_objects()

def get_specific_id():
    url = "https://api.restful-api.dev/objects/7"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    print("status code :", response.status_code)
    print("status reponse :", response.json())

#get_specific_id()

def add_new_object():

    url = "https://api.restful-api.dev/objects"

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

    print(response.status_code)
    print(response.json())

#add_new_object()
"""
200
{'id': 'ff8081819c5368bb019c8b7f5c385797', 'name': 'Apple MacBook Pro 16', 'createdAt': 1771866905656, 'data': {'year': 2019, 'price': 1849.99, 'CPU model': 'Intel Core i9', 'Hard disk size':
"""

def create_new_details():
   

    url = "https://gorest.co.in/public/v2/users"

    payload = json.dumps({
    "name": "Sunil Kumar Ramakrishna",
    "gender": "male",
    "email": "sunil.ramakrishna123@15ce.com",
    "status": "active"
    })
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ad6b849f911b220a37b1218280ce88bfa087d8c8f82bee717fd58a47d40f1277'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json())
    print(response.status_code)


create_new_details()
# create_new_details()
# {"id":8384278,"name":"Tenali Kumar Ramakrishna","email":"tenali.ramakrishna123@15ce.com","gender":"male","status":"active"}
# {'id': 8384282, 'name': 'Sunil Kumar Ramakrishna', 'email': 'sunil.ramakrishna123@15ce.com', 'gender': 'male', 'status': 'active'}