import json

common_url = "https://api.restful-api.dev/objects"
single_obj_id = "7"

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