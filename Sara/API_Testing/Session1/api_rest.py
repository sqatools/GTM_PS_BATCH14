import requests

def get_objects():
    url = "https://api.restful-api.dev/objects"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

get_objects()