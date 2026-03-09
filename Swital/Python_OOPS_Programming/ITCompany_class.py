class ITCompany:
    def __init__(self, comp_name, comp_Address, company_status, start_time, end_time):
        self.c_name = comp_name
        self.c_address = comp_Address
        self.c_status = company_status
        self.starttime = start_time
        self.stoptime = end_time
    
    def data_shown(self):
        print("Company Name is", self.c_name)
        print("Company Address is", self.c_address)
        print("Company Status is", self.c_status)

    def company_starttime(self):
        print(self.starttime, "of company")
    
    def company_stoptime(self):
        print(self.stoptime, "of the company")

itcomp = ITCompany("Wipro", "Banglore", "Active", "10:00Am", "7.00Pm")
itcomp.data_shown()
itcomp.company_starttime()
itcomp.company_stoptime()