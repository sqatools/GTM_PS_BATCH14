import json

gorest_url = "https://gorest.co.in/public/v2/users"

new_user_payload = json.dumps({
    "name": "Sohan Kumar Ramakrishna",
    "gender": "male",
    "email": "Sohan.ramakrishna123@15ce.com",
    "status": "active"
    })

auth_headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ad6b849f911b220a37b1218280ce88bfa087d8c8f82bee717fd58a47d40f1277'
    }