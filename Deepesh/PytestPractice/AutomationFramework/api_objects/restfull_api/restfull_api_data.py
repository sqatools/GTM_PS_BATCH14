import json

common_url = "https://api.restful-api.dev/objects"
single_obj_id = '7'
single_obj_id2 ='9'

create_new_object_payload = json.dumps({
  "name": "Apple MacBook Pro 16",
  "data": {
    "year": 2019,
    "price": 1849.99,
    "CPU model": "Intel Core i9",
    "Hard disk size": "1 TB"
  }
})

new_object_headers = {
    'Content-Type': 'application/json'
    }


create_new_object_payload2 = json.dumps({
  "name": "Apple MacBook Pro 20",
  "data": {
    "year": 2020,
    "price": 1849.99,
    "CPU model": "Intel Core i9",
    "Hard disk size": "1 TB"
  }
})

#########################################
gorest_url = "https://gorest.co.in/public/v2/users"

new_user_payload = json.dumps({
    "name": "Mohan Kumar Ramakrishna",
    "gender": "male",
    "email": "Mohan.ramakrishna123@15ce.com",
    "status": "active"
    })

auth_headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ad6b849f911b220a37b1218280ce88bfa087d8c8f82bee717fd58a47d40f1277'
    }