# install openpyxl package if not already installed
# pip install openpyxl
import openpyxl
def read_excel_file(file_path, sheet_name, cell_name):
    # Load the workbook
    workbook = openpyxl.load_workbook(file_path)
    # Select the specified sheet
    sheet = workbook[sheet_name]
    # Read the value from the specified cell
    cell_value = sheet[cell_name].value
    print(f"Value in {cell_name} of sheet '{sheet_name}': {cell_value}")
# read one cell data 
read_excel_file(file_path='Read_Excel.xlsx', sheet_name='Sheet1', cell_name='A2')

# get all rows and columns from excel sheet
for i in range(1, 6):
    read_excel_file(file_path='Read_Excel.xlsx', sheet_name='Sheet1', cell_name=f'A{i}')

#### Write data to excel file
def write_excel_file(file_path, sheet_name, cell_name, value):  
    # Load the workbook
    workbook = openpyxl.load_workbook(file_path)
    # Select the specified sheet
    sheet = workbook[sheet_name]
    # Write the value to the specified cell
    sheet[cell_name] = value
    # Save the workbook
    workbook.save(file_path)
    print(f"Wrote '{value}' to {cell_name} of sheet '{sheet_name}'")
# write one cell data
write_excel_file(file_path='Read_Excel.xlsx', sheet_name='Sheet1', cell_name='B2', value='Hello, World!')