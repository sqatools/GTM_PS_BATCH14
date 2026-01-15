"""
File read mode examples in Python.
1. read (r): Reads the entire file content.
2. write(w): Writes data to a file (overwrites existing content).
3. append(a): Appends data to the end of the file, and does not overwriote existing content.
"""
def readfile(file_path):
     # open file in read mode (r)
    # open will return a io.TextIOWrapper object
    file_obj= open(file_path,'r')
    file_data=file_obj.read() # Read the entire file content
    print("file content:",file_data)
    file_obj.close() # close the file

# read file from current directory
readfile(file_path='ABC.txt')

def writefile(file_path, data):
    # open file in write mode (w)
    file_obj= open(file_path,'w')
    file_obj.write(data) # Write data to the file
    print("Data written to file successfully.")
    file_obj.close() # close the file

# write data to existing file : this will overwrite existing content
new_data="Hema is learning python file handling."
writefile(file_path='ABC.txt',data=new_data)
