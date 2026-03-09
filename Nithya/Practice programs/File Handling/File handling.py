"""
File read mode examples in Python.
1. read (r): Reads the entire file content.
2. write(w): Writes data to a file (overwrites existing content).
3. append(a): Appends data to the end of the file, and does not overwrite existing content.
"""

def read_file(file_path):
    # open file in read mode (r)
    # open will return a io.TextIOWrapper object
    file_obj = open(file_path, 'r')
    file_data = file_obj.read() # Read the entire file content
    print("file content:", file_data)
    file_obj.close() # close the file

# read file from current directory
# read_file(file_path='read_data.txt')

# read file from different directory path
# read_file(file_path=r"E:\Filesdata\Batch14\count_name.txt")


'''
######################################################################
# write content to the file
def write_file(file_path, data):
    # open file in write mode (w)
    file_obj = open(file_path, 'w')
    file_obj.write(data) # Write data to the file
    print("Data written to file successfully.")
    file_obj.close() # close the file

# write data to existing file : this will overwrite existing content
new_data = "we are learning python file handling."
#write_file(file_path='abc.txt', data=new_data)

# write data to new file : this will create a new file
# write_file(file_path='newfile.txt', data=new_data)


######################################################################
# append content to the file
def append_file(file_path, data):
    # open file in append mode (a)
    file_obj = open(file_path, 'a')
    file_obj.write(data) # Append data to the file
    print("Data appended to file successfully.")
    file_obj.close() # close the file


# append data to existing file: this will not overwrite existing content and add data at the end of the file
append_data = "\nThis is appended line. adding with append mode."
#append_file(file_path='xyz.txt', data=append_data)

# append data to new file: this will create a new file
# append_file(file_path='appendfile.txt', data=append_data)


######################################################################
# context manager to handle file operations: context manager will automatically close the file after operations
def read_file_context_manager(file_path):
    # open file in read mode (r) using context manager
    with open(file_path, 'r') as file_obj:
        file_data = file_obj.read() # Read the entire file content
        print(file_data)
        print("Is file closed:", file_obj.closed) # Check if file is closed inside context manager
    print("Is file closed after context manager:", file_obj.closed) # Check if file is closed outside context manager


#read_file_context_manager(file_path='appendfile.txt')


#########################################################################
# Different methods to read file content
# 1. read with number of characters
def read_file_with_size(file_path, size):
    with open(file_path, 'r') as file_obj:
        # Read specified number of characters
        file_data = file_obj.read(size) 
        print(f"Read {size} characters: {file_data}, Length: {len(file_data)}")


read_file_with_size(file_path="read_data.txt", size=30)


# 2. readline: Read one line at a time
def read_file_line_by_line(file_path, lines):
    # Read specified number of lines
    with open(file_path, 'r') as file_obj:
        for i in range(lines):
            line_data = file_obj.readline()
            print(line_data)

#read_file_line_by_line(file_path="read_data.txt", lines=5)


# 3. readlines: Read all lines into a list  
def read_file_lines_as_list(file_path, line_no):
    with open(file_path, 'r') as file_obj:
        lines_list = file_obj.readlines() # Read all lines into a list
        #print("Lines in file as list:", lines_list)
        print(lines_list[line_no])

    
read_file_lines_as_list(file_path="read_data.txt", line_no=-1)

'''