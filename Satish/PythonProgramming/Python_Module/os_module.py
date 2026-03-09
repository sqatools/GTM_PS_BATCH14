"""
The os module in Python is a built-in standard library used to interact with the operating system. It is commonly used for file handling, directory management, environment variables, and process-level operations.
"""
import os

#Get current working directory

cwd=os.getcwd()
print(cwd)

#Create a New Directory
#os.mkdir('new_directory') #we can give path where we want to make directory

#Check file or folder(directory) exists

file_path=r'C:\AutomationProject\GTM_PS_BATCH14\Satish\PythonProgramming\Python_Module\os_module.py'
folder_path=r'C:\AutomationProject\GTM_PS_BATCH14\Satish\PythonProgramming\Python_Module\new_directory'

print("file path exist",os.path.exists(file_path)) #file path exist True
print("folder path exist",os.path.exists(folder_path)) #folder path exist True We can use if else to check whether file of directory exist or not

# check given path is file or directory

print(os.path.isfile(file_path)) # True
print(os.path.isfile(folder_path)) # False because it is a folder

#Build path
file_path=os.path.join('C','satish','1.xlsx')
print("File path",file_path) #C\satish\1.xlsx

#Get list of file and folder in a directory
path3= r'C:\AutomationProject\GTM_PS_BATCH14\Satish\PythonProgramming\Python_Module'
list1=os.listdir(path3)
print(list1) #['new_directory', 'os_module.py']

# Get count of file and folder in a directory(folder)

file_count=[]
folder_count=[]
#path4=r'C:\AutomationProject\GTM_PS_BATCH14\Satish\PythonProgramming\Python_Module'
path4 = r"C:\Testdata"
list_of_items=os.listdir(path4)
print("list of itens",list_of_items) #['new_directory', 'os_module.py']

for item in list_of_items:
    item_path = os.path.join(path4, item)
    print(item_path)
    if os.path.isfile(item_path):
        file_count.append(item)
    elif os.path.isdir(item_path):
        folder_count.append(item)
print("filecount",len(file_count))
print("folder count",len(folder_count))

"""
os.system(command) is a function in Python used to execute operating system (shell) commands from within a Python script.

"""

# os.system('dir')
# os.system('control') # This command will open control panel
# os.system("notepad")  # This will open Notepad application
os.system("cmd")     # This will open Command Prompt
os.system('systeminfo')
os.system('date')