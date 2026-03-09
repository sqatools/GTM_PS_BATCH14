import os
# Get current working directory
current_directory = os.getcwd()
print(f"Current Working Directory: {current_directory}")    
# this will print the current working directory path
# Swital/Python_Modules/OS_module

############################################################
print("_" * 50 )
# List all files and directories in the current directory
src_path = r"E:\Automation"
items_in_directory = os.listdir(src_path) # total items: 65
print("total items:", len(items_in_directory))
print("Items in Current Directory:")
for item in items_in_directory:
    print(item)

############################################################
print("_" * 50 )
# Create a new directory
#os.mkdir("new_directory")
#print("New directory 'new_directory' created.")
#os.mkdir(r"E:\Automation\Os_Operations\test_dir")

# multiple directories creation
#os.makedirs(r"E:\Automation\Os_Operations\parent_dir\child_dir1\child_dir2")
#print("Multiple directories created under 'parent_dir'.")  

#########################################3
# remove a directory
"""
os.rmdir(r"E:\Automation\Os_Operations\test_dir")
os.removedirs(r"E:\Automation\Os_Operations\parent_dir\child_dir1\child_dir2")
print("Directories removed successfully.")
"""
##################################################
print("*" * 50 )
# check file or directory exists
file_path = r"E:\Automation\git.txt" 
file_path2 = r"E:\Automation\Os_Operations\count_name.txt"
folder_path = r"E:\Automation\Os_Operations"    
print("check file exists:", os.path.exists(file_path))  # True
print("check file exists:", os.path.exists(file_path2))  # False
print("check folder exists:", os.path.exists(folder_path))  # True

####################################################################
# check given path is file or directory
print("-" * 50 )
path1 = r"E:\Automation\git.txt"
path2 = r"E:\Automation\Os_Operations"
print("Is file_path a file?", os.path.isfile(file_path))  # True
print("Is folder_path a directory?", os.path.isdir(folder_path))  # True
if os.path.isfile(path2):
    print(f"{path2} is a file.")
else:
    print(f"{path2} is not a file.")
# get count files and folders in a directory
print("-" * 50 )
path1 = r"E:\Automation"
list_items = os.listdir(path1)
file_count = []
folder_count = []
for item in list_items:
    item_path = os.path.join(path1, item)
    if os.path.isfile(item_path):
        file_count.append(item)
    elif os.path.isdir(item_path):
        folder_count.append(item)   
print(f"Total files: {len(file_count)}")
print(f"Total folders: {len(folder_count)}")    
############################################################
print("-" * 50 )
items = os.listdir(src_path)    
file_count = sum(1 for item in items if os.path.isfile(os.path.join(src_path, item)))
folder_count = sum(1 for item in items if os.path.isdir(os.path.join(src_path, item)))
print(f"Total files: {file_count}")
print(f"Total folders: {folder_count}")
############################################################
print("_" * 50 )
os.system("notepad.exe")  # This will open Notepad application
os.system("calc.exe")    # This will open Calculator application