"""
File read mode examples in Python.
1. read (r): Reads the entire file content.
2. write(w): Writes data to a file (overwrites existing content).
3. append(a): Appends data to the end of the file, and does not overwriote existing content.
"""

def read_file(file_path):
    file_obj=open(file_path,'r') # open function return a object
    file_data=file_obj.read() ## Read the entire file content
    print("file contents",file_data)
    file_obj.close() ## close the file

# read file from current directory then give only file name
#read_file('read_data.txt')

# if read from different directory then give full path

read_file(r'C:\AutomationProject\GTM_PS_BATCH14\Satish\first_file.txt') # we have use r(row string) here to null the effect 0f \n ,\t etc


##############################################################
# Write content to the file
def write_file(file_path,data):
    file_obj=open(file_path,'w')
    file_obj.write(data) # Write data to the file
    file_obj.close()  ## close the file


write_file('abc.txt',"We are learning python") # It will create new file with name as abc.txt if there is no file available of this name and write data "We are learning python" in this file

#If we again write in this file 'abc.txt' then it will overwite data

write_file('abc.txt',"Old data has been overwrite")

######################################################################
# append content to the file

def append_file(file_path,data):
    file_obj=open(file_path,'a')
    file_obj.write(data) # Append data to the file
    file_obj.close()  ## close the file

append_file('abc.txt',"\nThis is appended data")


######################################################################
# context manager to handle file operations: context manager will automatically close the file after operations so no need to close file if we use this

def read_file_with_context_manager(filepath):
    with open(filepath,'r') as file_obj:
        file_data=file_obj.read()
        print(file_data)

read_file_with_context_manager('read_data.txt')


#########################################################################************
# Different methods to read file content
# 1. read  number of characters from file

def read_file_with_no_of_character(filepath,character):
    with open(filepath,'r') as file_obj:
        file_data=file_obj.read(character)
        print(f"No of Character are {character} and content of file is {file_data}")

read_file_with_no_of_character('read_data.txt',5)


# 2. read  one line from file

def read_one_line(filepath):
    with open(filepath,'r') as file_obj:
        file_data=file_obj.readline()
        print(f"contents of file is {file_data}")

read_one_line('read_data.txt')


# 3. Read multiple lines from file

def read_multiple_lines(filepath,lines):
    with open(filepath,'r') as file_obj:
        for line in range(lines):
            line_data=file_obj.readline()
            print(line_data)

read_multiple_lines('read_data.txt',4)


# Read All lines from file into a list

def read_all_lines(filepath):
    with open(filepath,'r') as file_obj:
        line_list=file_obj.readlines()  # Noted here method name is readlines
        print(line_list)

read_all_lines('read_data.txt')
