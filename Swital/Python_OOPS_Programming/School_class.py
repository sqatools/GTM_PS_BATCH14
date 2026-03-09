class School:
    def __init__(self,name, fee, address):
        self.name1 = name
        self.fee1 = fee
        self.address1 = address
    
    def display_schooldata(self):
        print("School name is", self.name1)
        print("School fee is", self.fee1)
        print("School address is", self.address1)
    
    def school_faculty(self):
        print("Address is", self.address1)
    
    def school_time(self):
        print(self.name1, "time is 10am")

school = School("St. Xaviers", 12000, "Delhi")
school.display_schooldata()
school.school_faculty()
school.school_time()