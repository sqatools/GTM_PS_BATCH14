import json
common_url = "https://api.restful-api.dev/objects"
single_obj_id = '7'
single_obj_id2 = '9'

new_object_headers = {
    'x-api-key': '',
    'Content-Type': 'application/json'
    }


create_new_object_payload =json.dumps( {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
})

create_new_object_payload2 = json.dumps({
    "name": "Apple iPad Air",
    "data": {
        "year": 2022,
        "price": 599.99,
        "CPU model": "Apple M1",
        "Hard disk size": "256 GB"
    }
})

auth_headers = {
    "Authorization": "ec4740da494f2f188f7ea2ca826e4fa8c4d2411b61c8d164add2e266c3a64e78",
    'x-api-key': '',
        
    "Content-Type": "application/json"
    
}

new_user_payload = json.dumps( {
    "name": "Teena Ramakrishna",
    "email": "teena@example.com",
    "gender": "male",
    "status": "active"
})
############################################
gorest_url = "https://gorest.co.in/public/v2/users"

new_user_payload = json.dumps({
    "name": "Hello API",
    "gender": "male",
    "email": "HelloAPI12@15ce.com",
    "status": "active"
    })

auth_headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ec4740da494f2f188f7ea2ca826e4fa8c4d2411b61c8d164add2e266c3a64e78'
    }