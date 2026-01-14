'''
In file handling , there are 3 modes to handle file operations:
1.read(r):Reads the entire file content.
2.write(w):writes data to a file and overwrites if if the files alrerady present
3.append(a):Appends data to the file and does not over write the contect.
'''

def read_file(file_path):
    #open file inn read mode(r) and storing the return value in file_object
    file_obj=open(file_path,'r')
    #read the entire file content
    file_content=file_obj.read()
    print("My First File ,:",file_content)
    file_obj.close

#read file from current directory
#read_file(file_path='sample.txt')

#reading a file from the different directoy path
#read_file(file_path="C:\Sample\File_handling\Random.txt")

##############################################################
#Using Write mode('w') to write the content into the file

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

def append_file(file_path, data):
    file_obj=open(file_path,'a')
    file_obj.write(data)
    print("Data appended successfully")
    file_obj.close()

append_file(file_path='abc.txt',data="\nThis is appended line. adding with append mode.")
