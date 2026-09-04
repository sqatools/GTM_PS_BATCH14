
class School():
    def __init__(self, name="Grayston", fee="5000", address="Sandton"):
        print("This is a School class.")
        self.name = name
        self.fee = fee
        self.address = address

    def start_class(self):
        print(self.name, "is started")

    def close_school(self):
        print(self.name, "is closed")

    def displayschool_details(self):
        print(f"School Name:{self.name},School Fee:{self.fee},School Address:{self.address}")
        
        
        
