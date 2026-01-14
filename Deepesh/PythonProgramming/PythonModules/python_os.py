import os
# This script demonstrates basic usage of the os module in Python.

# Get the current working directory
current_directory = os.getcwd()
print(f"Current Working Directory: {current_directory}")
# this will print the current working directory path
# E:\Trainings\GTM_PS_Batch14_7Nov25\GTM_PS_BATCH14\Deepesh\PythonProgramming\PythonModules


############################################################
print("_" * 50 )
# List all files and directories in the current directory
src_path = r"E:\Filesdata"
items_in_directory = os.listdir(src_path) # total items: 65
print("total items:", len(items_in_directory))
print("Items in Current Directory:")
for item in items_in_directory:
    print(item)

############################################################
print("#" * 50 )
# Create a new directory
#os.mkdir("new_directory")
print("New directory 'new_directory' created.")

#os.mkdir(r"E:\Filesdata\Os_Operations\test_dir")


# multiple directories creation
#os.makedirs(r"E:\Filesdata\Os_Operations\parent_dir\child_dir1\child_dir2")
print("Multiple directories created under 'parent_dir'.")

# remove a directory
"""
os.rmdir("new_directory")
os.removedirs(r"E:\Filesdata\Os_Operations\parent_dir\child_dir1\child_dir2")

print("Directories removed successfully.")
"""
####################################################################
print("*" * 50 )
# check file or directory exists
file_path = r"E:\Filesdata\count_name.txt" 
file_path2 = r"E:\Filesdata\Os_Operations\count_name.txt"
folder_path = r"E:\Filesdata\Os_Operations"

print("check file exists:", os.path.exists(file_path))  # True
print("check file exists:", os.path.exists(file_path2))  # False
print("check folder exists:", os.path.exists(folder_path))  # True

####################################################################
# check given path is file or directory
print("-" * 50 )

path1 = r"E:\Filesdata\count_name.txt"
path2 = r"E:\Filesdata\Os_Operations"
#print("Is file_path a file?", os.path.isfile(file_path))  # True
#print("Is folder_path a directory?", os.path.isdir(folder_path))  # True

if os.path.isfile(path1):
    print(f"{path1} is a file.")
else:
    print(f"{path1} is not a file.")


# get count files and folders in a directory
print("-" * 50 )
path1 = r"E:\Filesdata"
list_items = os.listdir(path1)
file_list = []
folder = []

for item in list_items:
    item_path = os.path.join(path1, item)
    print(item_path)
    if os.path.isfile(item_path):
        file_list.append(item)
    elif os.path.isdir(item_path):
        folder.append(item)

print("Total files:", file_list)
print("Total files:", len(file_list))
print("total folders:", folder)
print("Total folders:", len(folder))


####################################################################
# execute commands in os module
print("-" * 50 )

"""
os.system("notepad")  # This will open Notepad application
os.system("calc")    # This will open Calculator application
os.system("cmd")     # This will open Command Prompt
os.system("control")  # This will open Control Panel
"""

os.system("python hello_world.py")
os.system("python E:\Trainings\GTM_PS_Batch14_7Nov25\GTM_PS_BATCH14\Deepesh\PythonProgramming\Python_String\hello_world.py")
