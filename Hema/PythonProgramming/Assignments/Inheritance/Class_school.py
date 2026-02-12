class School:
    def __init__(self, Name, Fees, Address):        
        self.Name = Name
        self.Fees = Fees
        self.Address = Address

    def Show_School_Name(self):
        print(f"School name is {self.Name}")    

    def Show_School_Fees(self):
        print(f"School fees is {self.Fees}")

    def Show_School_Address(self):
        print(f"School address is {self.Address}")
    
# creating an object of the School class