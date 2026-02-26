import requests

def get_all_objets():
    import requests

    url = "https://api.restful-api.dev/objects"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

get_all_objets()


def post_method_for_objects():

    url = "https://gorest.co.in/public/v2/users"

    payload = {
        "name":"Hemag P",
        "email":"hema@fay-swift.example",
        "gender":"male",
        "status":"inactive"
    }
    headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 24102ac93872ef791b3b1cefb2dca817fbb8e681552e32a38d96e0d09af98927"
    }


    response = requests.request("POST", url, headers=headers, json=payload)

    print(response.text)

post_method_for_objects()

def post_method_for_restful_api_objects():

    url = "https://api.restful-api.dev/objects"

    payload = {
  "name": "Hema's Apple MacBook Pro 16",
  "data": {
    "year": 2025,
    "price": 2000.00,
    "CPU model": "Intel Core i9",
    "Hard disk size": "2 TB"
  }
}
    headers = {
    "Content-Type": "application/json"
    }


    response = requests.request("POST", url, headers=headers, json=payload)

    print(response.text)

post_method_for_restful_api_objects()
