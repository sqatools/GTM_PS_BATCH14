'''
https://gorest.co.in/

https://gorest.co.in//public/v2/users

'''

import requests
import json

def create_new_user():

    url = "https://gorest.co.in/public/v2/users"

    payload = json.dumps({
    "name": "Sara Ramakrishna",
    "gender": "Female",
    "email": "sara.ramakrishna@15ce.com",
    "status": "active"
    })
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 19df031a38111bc481b6ac57716de1ebdf3d2e4e5093dd6b4f6755aade883554'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


create_new_user()

'''
PS C:\PythonAutomationProject\GTM_PS_BATCH14\Sara\API_Testing\Sesson2> python .\api_create_user.py
{"id":8385161,"name":"Sara Ramakrishna","email":"sara.ramakrishna@15ce.com","gender":"female","status":"active"}
PS C:\PythonAutomationProject\GTM_PS_BATCH14\Sara\API_Testing\Sesson2> 
'''

