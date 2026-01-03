"""
File read mode examples in Python.
1. read (r): Reads the entire file content.
2. write(w): Writes data to a file (overwrites existing content).
3. append(a): Appends data to the end of the file, and does not overwriote existing content.
"""

import os

def read_file(file_path):
    # open file in read mode (r)
    # open will return a io.TextIOWrapper object
    file_obj = open(file_path, 'r')
    file_data = file_obj.read() # Read the entire file content
    print("file content:", file_data)
    file_obj.close() # close the file
# read file from current directory
read_file(file_path='read_data.txt') 

# read file from different directory path
external_path = r"E:\Growtechmind\All Exception.txt"
if os.path.exists(external_path):
    read_file(file_path=external_path)
else:
    print(f"Skipping missing file: {external_path}")

# Write content to the file: overwrites existing content
def write_file(file_path, data):
    # open file in write mode (w)
    file_obj = open(file_path, 'w')
    file_obj.write(data) # Write data to the file
    print("Data written to file successfully.")
    file_obj.close() # close the file}
# write data to existing file : this will overwrite existing content
new_data = "we are learning python file handling."
write_file(file_path='abc.txt', data=new_data)
# write data to new file : this will create a new file
write_file(file_path='newfile.txt', data=new_data)
