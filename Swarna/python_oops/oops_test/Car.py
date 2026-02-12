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


class Car:
    def __init__(self, name, price, company):
        self.name = name
        self.price = price
        self.company = company

    def display_info(self):
        print("Car Name:", self.name)
        print("Price:", self.price)
        print("Company:", self.company)
    
    def calculate_tax(self):
        tax = self.price * 0.10
        print(f"Tax for {self.name}: ${tax}")
        return tax
    
    def apply_discount(self, discount_percent):
        discount = self.price * (discount_percent / 100)
        final_price = self.price - discount
        print(f"{self.name} after {discount_percent}% discount: ${final_price}")
        return final_price