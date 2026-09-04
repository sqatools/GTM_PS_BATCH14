
def read_file(file_path):
    file_obj = open(file_path, 'r')
    file_data = file_obj.read() 
    print("file content:", file_data)
    file_obj.close() 


read_file(file_path='read_data.txt')