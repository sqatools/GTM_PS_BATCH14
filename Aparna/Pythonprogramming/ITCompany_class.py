class ITCompany():
    def __init__(self, Company_name="Cybage", Company_address="Pune", Company_status="IT"):
        print("This is a IT Company class.")
        self.Company_name = Company_name
        self.Company_address = Company_address
        self.Company_status = Company_status

    def dev_software(self):
        print("Software is being deployed")

    def test_aaplication(self):
        print("Application is being tested and deploy to prod")

    def ITCompany_details(self):
        print(f"Company Name:{self.Company_name},Company address:{self.Company_address},Company status:{self.Company_status}")