"""1. Create five 5 different classes in 5 different files
  ->  Car (name, price, company)
  ->  School (name, fee, address)
  ->  ITCompany (comp_name, comp_Address, company_status)
  ->  HRDepart (recruirment, training, activity)
  ->  Hotel (Hotelname, hoteladdress, roomprice)
2. Each class contains 3 menthods
3. Create ManagementClass in the 6th file and import all 5 files classes in one class.
   ->  create object of all the classes in one class
   ->  through class ManagementClass object access all different method."""
class Car :
    def __init__(self, name, price, company):
        self.name = name
        self.price = price      
        self.company = company
        
    def display_name(self):
        print(f"Car name: {self.name}")

    def display_price(self):
        print(f"Car price: {self.price}")   

    def display_company(self):
        print(f"Car company: {self.company}")