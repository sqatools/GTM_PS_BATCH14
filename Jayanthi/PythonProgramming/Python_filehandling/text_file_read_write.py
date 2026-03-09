# read the file 
def read_file(filepath):
    file_obj = open(filepath, 'r')
    file_data = file_obj.read() # Read the entire file content
    print("file content:", file_data)
    file_obj.close() # close the file

read_file(filepath='Jayanthi/PythonProgramming/Python_filehandling/test.txt')   

#Write the file
def write_file(filepath, data):
    # open file in write mode (w)
    file_obj = open(filepath, 'w')
    file_obj.write(data) # Write data to the file
    print("Data written to file successfully.")
    file_obj.close() # close the file

new_data = "We are learning python file handling."
write_file(filepath='Jayanthi/PythonProgramming/Python_filehandling/test.txt', data=new_data)    

#Append the file
def append_file(filepath, data):
    # open file in append mode (a)
    file_obj = open(filepath, 'a')
    file_obj.write(data) # Append data to the file
    print("Data appended to file successfully.")
    file_obj.close() # close the file
append_data = "\nThis is appended line. adding with append mode."
append_file(filepath='Jayanthi/PythonProgramming/Python_filehandling/test.txt', data=append_data)

# context manager to handle file operations: context manager will automatically close the file after operations
def read_file_context_manager(filepath):
    # open file in read mode (r) using context manager
    with open(filepath, 'r') as file_obj:
        file_data = file_obj.read() # Read the entire file content
    print(file_data)
    print("Is file closed:", file_obj.closed) # Check if file is closed inside context manager
    print("Is file closed after context manager:", file_obj.closed) # Check if file is closed outside context manager   
read_file_context_manager(filepath='Jayanthi/PythonProgramming/Python_filehandling/test.txt')   
######################################################################
"""Python File Handling Modes:"""
"""
1. read(r): Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
2. write(w): Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
3. append(a): Appends data to the end of the file, and does not overwriote existing content.
"""


