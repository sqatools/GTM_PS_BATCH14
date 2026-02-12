

class School:
    def __init__(self,name,fees,address):
        self.name=name
        self.fees=fees
        self.address=address

    def rank(self):
        print("It is no 1 school of city")

    def standatd(self):
        print("This school is up to class 10th standard")

    def details(self):
        return self.name,self.fees,self.address



