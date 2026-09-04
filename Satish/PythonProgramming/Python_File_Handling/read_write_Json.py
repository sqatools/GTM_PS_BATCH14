# read write json file
# Note: In json file string key should be in double quotes where as in dictionary we can put in single quote
import json

def read_json_file(file_path):
    with open(file_path,'r') as json_file_obj:
        json_file_data=json.load(json_file_obj)
        print(json_file_data)
        print(json_file_data['employees'][0]['id'])

read_json_file('emp_data.json')

def write_json_file(file_path,data):
    with open(file_path,'w') as json_file_obj:
        json.dump(data,json_file_obj)

user_data={
    "users":[{"username":"user1","password":"pass1"},{"username":"user2","password":"pass2"},{"username":"user3","password":"pass3"},{"username":"user4","password":"pass4"}]
}

write_json_file('user_data.json',user_data) # give any .json file name if file is not available it will create it