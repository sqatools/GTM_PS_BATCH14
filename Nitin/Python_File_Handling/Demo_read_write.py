# context manager to handle file operations: context manager will automatically close the file after operations
def read_file_contetext_manager(filename):
    with open(filename,'r') as file_object:
        file_content=file_object.read()
        print("File content:",file_content)
        print(file_object.closed)
    print(file_object.closed)

#read_file_contetext_manager('sample.txt')
def read_file_with_size(file_path, size):
    with open(file_path, 'r') as file_obj:
        # Read specified number of characters
        file_data = file_obj.read(size) 
        print(file_data)
        print(f"Read {size} characters: {file_data}, Length: {len(file_data)}")


#read_file_with_size(file_path="read_data.txt", size=30)

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
        print("Lines in file as list:", lines_list)
        print("1st 3 lines:",lines_list[0:3])
        print("Last 3 lines:",lines_list[-3:])
        print(lines_list[line_no])

    
#read_file_lines_as_list(file_path="read_data.txt", line_no=2)
#Program to get the file’s first three and last three lines
def read_file(file_path):
    file_obj=open(file_path,'r')
    file_content=file_obj.readlines() #readlines willreturn the list of lines.
    for i in file_content:
        #print(i)
        print("Reading the first 3 lines:",file_content[0:3])
        break 
        #print("Reading the first 3 lines:")
    file_obj.close()

#read_file(file_path="xyz.txt")


def read_file_alternate(file_path):
    file_obj=open(file_path,'r')
    file_content=file_obj.readlines()
    for i in file_content[:3]:
        print(i)

    for i in file_content[-3:]:
        print(i)
    file_obj.close()
read_file_alternate(file_path="xyz.txt")
