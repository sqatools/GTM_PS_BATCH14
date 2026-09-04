import requests
import json

def post_api_request():

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

post_api_request()    

"""
PS C:\PythonAutomationProject\GTM_PS_BATCH14\Sara\API_Testing\Session1> python .\api_post.py
200
{'id': 'ff8081819c5368bb019c909c218e620d', 'name': 'Apple MacBook Pro 16', 'createdAt': 1771952677262, 'data': {'year': 2019, 'price': 1849.99, 'CPU model': 'Intel Core i9', 'Hard disk size': '1 TB'}}

"""