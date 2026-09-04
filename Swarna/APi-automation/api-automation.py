import requests

def get_all_objects_api():
    url = "https://api.restful-api.dev/objects"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


get_all_objects_api()


def add_new_object():
    import requests
    import json

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

add_new_object()