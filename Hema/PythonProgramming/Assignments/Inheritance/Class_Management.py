from Class_car import Car
from Class_school import School
from Class_Hotel import Hotel
from Class_ITCompany import ITCompany
from Class_HRDepartment import HRDepartment
    
class Management():
    def __init__(self):
    # here create object of all the classes in one class
       self.car = Car("BMW", 100000, "Germany")
       self.school = School("DAV Public School", 50000, "Pune")
       self.hotel = Hotel("Taj", "Mumbai", 10000)
       self.itcompany = ITCompany("TCS", "Pune", "Active")
       self.hrdepartment = HRDepartment("Recruitment", "Training", "Activities")

    def create_objects(self):
       self.car1 = Car("BMW", 100000, "Germany")
       self.school1 = School("DAV Public School", 50000, "Pune")
       self.hotel1 = Hotel("Taj", "Mumbai", 10000)
       self.itcompan1 = ITCompany("TCS", "Pune", "Active")
       self.hrdepartment1 = HRDepartment("Recruitment", "Training", "Activities")
        
      
#create object of management class and through class ManagementClass object access all different method.
result = Management()
# Access all methods through Management object
#car
result.create_objects() # Create objects of all classes

result.car1.display_name()
result.car1.display_price() 
result.car1.display_company()


result.car.display_name()
result.car.display_price()
result.car.display_company()
#school
result.school.Show_School_Name()
result.school.Show_School_Fees()
result.school.Show_School_Address()
#hotel
result.hotel.Show_Hotel_Name()
result.hotel.Show_Hotel_Address()
result.hotel.Show_Room_Price()
#ITCompany
result.itcompany.Show_Company_Name()                    
result.itcompany.Show_Company_Address()
result.itcompany.Show_Company_Status()
#HRDepartment
result.hrdepartment.Show_Recruitment()          
result.hrdepartment.Show_Training()
result.hrdepartment.Show_Activity() 


"""def show_all_details(self):
        self.car.display_name()
        self.car.display_price()
        self.car.display_company()

        self.school.Show_School_Name()
        self.school.Show_School_Fees()
        self.school.Show_School_Address()

        self.hotel.Show_Hotel_Name()
        self.hotel.Show_Hotel_Address()
        self.hotel.Show_Room_Price()

        self.itcompany.Show_Company_Name()
        self.itcompany.Show_Company_Address()
        self.itcompany.Show_Company_Status()

        self.hrdepartment.Show_Recruitment()
        self.hrdepartment.Show_Training()
        self.hrdepartment.Show_Activity()
result = Management()
result.show_all_details() """
    