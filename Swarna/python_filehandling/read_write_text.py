def read_file(file_path):
    """Reads the content of a text file and returns it."""
    with open(file_path, 'r') as file:
        content = file.read()
    return content


# data = read_file('read_data.txt')  # Replace 'example.txt' with your file path
# print(data) 

data2 = read_file('/Users/swarna/newtest/GTM_PS_BATCH14/Pooja/second_File.txt')  # Replace 'example.txt' with your file path
print(data2)