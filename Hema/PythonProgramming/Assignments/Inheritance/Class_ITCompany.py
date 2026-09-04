class ITCompany:
    def __init__(self, Company_name, Company_Address, Company_status):
        self.company_name = Company_name
        self.company_Address = Company_Address
        self.company_status = Company_status

    def Show_Company_Name(self):
        print(f"Company name is {self.company_name}")   

    def Show_Company_Address(self):
        print(f"Company address is {self.company_Address}")

    def Show_Company_Status(self):
        print(f"Company status is {self.company_status}")
    