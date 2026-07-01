
from Car_class import Car
from School_class import School
from ITCompany_class import ITCompany





class Main():
    
    def execute(self):
        #Create objects
        car = Car("Honda", "6.0L", "Honda")#thisis an normal variable
    #def __init__(self):
        #self.car=Car("Honda", "6.0L", "Honda")--this is an instance var
        school = School("Grayston", "5000", "Sandton")
        itcompany = ITCompany("Cybage", "Pune", "IT")
        #call car methods
        car.displaycar_details()
        car.starting_car()
        car.stopping_car()
        
        print("----------------------------")

        school.displayschool_details()
        school.start_class()
        school.close_school()
        
        print("----------------------------")

        itcompany.ITCompany_details()
        itcompany.dev_software()
        itcompany.test_aaplication()


#if __name__== "__main__":
#create object of main class
main = Main()
main.execute()#if const not their 
#if const their 
#main.car.displaycar_details()
#or else with classname if we dint create  object


print("module name :", main.__module__)

    