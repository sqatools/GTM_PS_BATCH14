"""
File read mode examples in Python.
1. read (r): Reads the entire file content.
2. write(w): Writes data to a file (overwrites existing content).
3. append(a): Appends data to the end of the file, and does not overwriote existing content.
"""

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
read_file(file_path=r"E:\Growtechmind\All Exception.txt")

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

# Append content to the file: does not overwrite existing content
def append_file(file_path, data):
    # open file in append mode (a)
    file_obj = open(file_path, 'a')
    file_obj.write(data) # Append data to the file
    print("Data appended to file successfully.")
    file_obj.close() # close the file
# append data to existing file: this will not overwrite existing content and add data at the end of the file
append_data = "\nFile handling is very important in python."    
append_file(file_path='abc.txt', data=append_data)
# append data to new file : this will create a new file 
append_file(file_path='appendfile.txt', data=append_data)

# context manager to handle file operations: context manager will automatically close the file after operations
def read_file_context_manager(file_path):
    # open file using context manager (in read mode)
    with open(file_path, 'r') as file_obj:
        # read file content
        file_data = file_obj.read()
        print("file content using context manager:", file_data)
        print("File is closed:", file_obj.closed) # check if file is closed
        print("Is file closed after context manager:", file_obj.closed) # check if file is closed after context manager
# read file using context manager   
read_file_context_manager(file_path='read_data.txt')

# # Different methods to read file content
# 1. Read with number of characters
def read_file_n_chars(file_path, size):
    with open(file_path, 'r') as file_obj:
        file_data = file_obj.read(size) # Read size characters from the file
        print(f"First {size} characters of the file:, {file_data}, Length: {len(file_data)}") 
# read first 10 characters from the file
read_file_n_chars(file_path='read_data.txt', size=10)

#2 Read with line by line using readline()
def read_file_line_by_line(file_path, lines):
    with open(file_path, 'r') as file_obj:
        for i in range(lines): # Read first 3 lines
            line_data = file_obj.readline()
            print("Line:", line_data) # Print the line without extra new line
        print("File reading completed.")

# 2. Read line by line using readline()
#def read_file_line_by_line(file_path):
#    with open(file_path, 'r') as file_obj:
#        line = file_obj.readline() # Read first line
#        while line:
#            print("Line:", line.strip()) # Print the line without extra new line
#            line = file_obj.readline() # Read next line 
# read file line by line
#read_file_line_by_line(file_path='read_data.txt')  

# 3. Read all lines using readlines()
def read_file_all_lines(file_path):
    with open(file_path, 'r') as file_obj:
        lines = file_obj.readlines() # Read all lines into a list
        for index, line in enumerate(lines):
            print(f"Line {index + 1}: {line.strip()}") # Print each line with line number
# read all lines from the file
read_file_all_lines(file_path='read_data.txt')  

# 4. Read file using for loop
def read_file_using_for_loop(file_path):
    with open(file_path, 'r') as file_obj:
        for index, line in enumerate(file_obj):
            print(f"Line {index + 1}: {line.strip()}") # Print each line with line number   
# read file using for loop
read_file_using_for_loop(file_path='read_data.txt') 

# 4. readlines: Read all lines into a list  
def read_file_lines_as_list(file_path, line_number):
    with open(file_path, 'r') as file_obj:
        lines = file_obj.readlines() # Read all lines into a list
        print("Lines as list:", lines) # Print the list of lines
        print("Number of lines:", len(lines)) # Print the number of lines
# read file lines as list
read_file_lines_as_list(file_path='read_data.txt', line_number=5)