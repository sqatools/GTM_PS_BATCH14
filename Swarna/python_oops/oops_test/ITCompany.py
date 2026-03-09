class ITCompany:
    def __init__(self, comp_name, comp_address, company_status):
        self.comp_name = comp_name
        self.comp_address = comp_address
        self.company_status = company_status

    def display_info(self):
        print("Company Name:", self.comp_name)
        print("Company Address:", self.comp_address)
        print("Company Status:", self.company_status)
    

    def hire_employee(self, employee_name):
        print(f"Employee {employee_name} hired at {self.comp_name}")
    
    def update_status(self, new_status):
        self.company_status = new_status
        print(f"{self.comp_name} status updated to: {new_status}")