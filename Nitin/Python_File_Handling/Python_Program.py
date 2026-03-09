#Program to get the file’s first three and last three lines
def read_file(file_path):
    file_obj=open(file_path,'r')#Opening the file in read mode
    file_content=file_obj.readlines()#readlines will return the list of lines.

    for i in file_content[:3]:
        print(i)
    print("---------")
    for i in file_content[-3:]:
        print(i)
    file_obj.close()
#read_file(file_path="xyz.txt")

#Python file program to get all the email ids from a text file.
def read_email_ids(file_path):
    file_obj=open(file_path,'r')
    file_content=file_obj.read()# read()will return the string data
    print(file_content)
    print("----------")
    list1=[]
    for i in file_content.split():# split() will split the string data based on space and return the list of words.
        #print(i)
        if i.endswith("@gmail.com")or i.endswith("yahoo.com"):
            print("Email id found in file :",i)
    file_obj.close()       
#read_email_ids(file_path="mnn.txt")

def read_email_ids_file(file_path):
    file_obj=open(file_path,'r')
    file_content=file_obj.read()#read() will return the string.
    print(file_content)
    for i in file_content.split(): # split() will convert the str in List 
        if i.endswith("gmail.com") or i.endswith("yahoo.com"):
            print("------")
            print(i)
    file_obj.close()
#read_email_ids_file(file_path="mnn.txt")

#Python file program to get a specific line from the file
def read_file_line(file_path):
    file_obj=open(file_path,'r')
    line=file_obj.readlines()# readlines() will return the list of lines.
    for i in line[3]:
        print(i , end="")
    file_obj.close()

#read_file_line(file_path="xyz.txt")

#Python file program to get odd lines from files and append them to separate files.
def read_odd_lines_files(file_path):
    file_obj=open(file_path,'r')
    lines=file_obj.readlines()# readlines willreturn the list of string lines.
    print(lines)
    odd_list=[]
    for i in lines[::2]:
        print(i)
        odd_list.append(i)
        file_obj.close()
    print("Odd lines list:",odd_list)
    
read_odd_lines_files(file_path="mnn.txt")

# Python file program to read a file line by line and store it in a list.
def read_file_to_line_list(file_path):
    file_obj=open(file_path,'r')
    line_list=file_obj.readlines()# readlines will store the list of lines.
    list1=[]
    for i in line_list:
        #print(i ,end='')
        list1.append(i)
    file_obj.close()
    print("List of lines ffrom a file store into a list:",list1)

#read_file_to_line_list(file_path="mnn.txt")

#Python file program to find the longest word in a file.
def find_longest_word(file_path):
    file_obj=open(file_path,'r')
    #line_list=file_obj.readlines()#readlines() will return the string into list of lines.
    file_content=file_obj.read().split()# read() will return the string data.
    print(file_content)
    longest_word=[]
    for i in file_content:
        if len(i)>len(longest_word):
            #longest_word=longest_word+
            longest_word=i
    print("Longest word in the file is:",longest_word)

#find_longest_word(file_path="abc.txt")

#Python file program to get the count of a specific word in a file.
def count_word_in_file(file_path):
    file_obj=open(file_path,'r')
    file_content=file_obj.readline()
    cout_word=file_content.count('is')
    print("Count of word 'is' in the file is:",cout_word)
    print(file_content)
    file_obj.close()

#count_word_in_file(file_path="abc.txt")

#file program to copy the file’s contents to another file after converting it to lowercase
def copy_file_content_another_file(source_file, dest_file):
    file_obj=open(source_file,'r')
    file_content=file_obj.readlines().lower()
    file_content.copy()(dest_file)
    file_obj.close()

copy_file_content_another_file(source_file="abc.txt", dest_file="dest.txt")

