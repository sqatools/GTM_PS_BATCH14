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

os.rmdir(r"E:\Automation\Os_Operations\test_dir")
os.removedirs(r"E:\Automation\Os_Operations\parent_dir\child_dir1\child_dir2")
print("Directories removed successfully.")

