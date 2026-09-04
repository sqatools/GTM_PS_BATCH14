# read JSON file
import json 
def read_json_file(file_path):
    # open json file in read mode
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)  # Load json data
        print("JSON data read from file:")
        print(data)

    return data
output = read_json_file(file_path='emp_data.json')
print("_"*50)
print(output["employees"][1])
print(output["employees"][1]["salary"])

# write JSON file
def write_json_file(file_path, data):   
    # open json file in write mode
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)  # Write json data to file with indentation
        print("JSON data written to file successfully.")    
user_data = {
    "users": [{"username": "user1", "password": "pass1"},
              {"username": "user2", "password": "pass2"},
              {"username": "user3", "password": "pass3"},
              {"username": "user4", "password": "pass4"},
              {"username": "user5", "password": "pass5"}]
}
write_json_file(file_path='user_data.json', data=user_data) 
