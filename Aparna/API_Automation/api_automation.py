"""
API: Aplication programming Interface
It an intreface between bussiness layerand database
https://restful-api.dev/
 
presentation layer
    |
business layer(API)
    |
database layer 


1. Free API : Everyone access it.
2. Private API : Specific Organasation(INTERNAL USRES)
3. Paid API : Businesses has to pay subscription fee to access API service. E.G AI 

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
import json
# pip install requests

def get_all_objects():

    url = "https://api.restful-api.dev/objects"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print("status code:",response.status_code)
    print("status response:",response.json()) 
   # assert len(response.json())==12,"Number is not as per theexpectation"  
    assert len(response.json())==13
    assert response.json()[-1]['id']=="13", "As expected"
    assert response.json()[-1]['name']=="Apple iPad Air"

#get_all_objects()



def get_specific_id():
    
    url = "https://api.restful-api.dev/objects/7"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    print("status code:",response.status_code)
    print("status response:",response.json()) 
   
    
    
#get_specific_id()
#https://restful-api.dev/

def add_data():
   

    url = "https://api.restful-api.dev/collections/products/objects"

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
    'x-api-key': '',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)
    print(response.json())
    
#add_data()

#https://gorest.co.in/rest-console--pratcie
def create_new_user():
    
    url = "https://gorest.co.in/public/v2/users"

    payload = json.dumps({
    "name": "DOO",
    "email": "Doo@example.com",
    "gender": "male",
    "status": "active"
    })
    headers = {
    'Authorization': 'Bearer 38e1be3fe2a94a291758cd6ae0a19c9c950a3191a663cf33001fdfae3e3d1064',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json())
    print(response.status_code)

create_new_user()