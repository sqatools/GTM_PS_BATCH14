"""
1. single inheritance : when one class inherits from another class then it is called single inheritance.
                        class A --> class B
2. multi-level inheritance :  when a class inherits from a derived class then it is called multi-level inheritance.
                      class A --> class B --> class C
3. multiple inheritance : when a class inherits from more than one class then it is called multiple inheritance.
                      class A --> class C  , class B --> class C"""
"""
Assignment 1: Basic Single Inheritance

Create:
A class Person with attributes name and age
A class Employee that inherits from Person
Add attribute employee_id to Employee
Create an object of Employee and display all details

Assignment 2: Multilevel Inheritance

Create:
Class Company
Class Department inheriting Company
Class Employee inheriting Department
Each class should have one unique method
Call all methods using an Employee object


Assignment 3: Method Inheritance

Create:
A base class "Vehicle" with a method start()
A derived class "Car" that inherits Vehicle
Call the start() method using a "Car" object

Assignment 4: Using super()

Create:
A class "Account" with attribute balance
A derived class "SavingsAccount"
Use super() to initialize balance
Add a method to display account details in SavingsAccount
create object of SavingsAccount and display details
"""

# single inheritance
"""Assignment 1: Basic Single Inheritance

Create:
A class Person with attributes name and age
A class Employee that inherits from Person
Add attribute employee_id to Employee
Create an object of Employee and display all details"""
"""
class Person(name,age):
    # parent class
    def person_info(self):
        print("This is person class")
class Employee(Person):
    # child class
    def employee_info(self):
        print("This is employee class")

obj = Employee()
obj.person_info()  # calling parent class method    
obj.employee_info()   # calling child class method
"""
"""Assignment 2: Multilevel Inheritance

Create:
Class Company
Class Department inheriting Company
Class Employee inheriting Department
Each class should have one unique method
Call all methods using an Employee object
"""
class Company:
    def company_info(Self):
        print("This is company class")
class Department(Company):
    def department_info(self):
        print("This is department class")   

class Employee(Department):
    def employee_info(self):
        print("This is employee class")
obj= Employee()
obj.company_info()  # calling parent class method    
obj.department_info()   # calling child class method        
obj.employee_info()   # calling child class method

"""Assignment 3: Method Inheritance

Create:
A base class "Vehicle" with a method start()
A derived class "Car" that inherits Vehicle
Call the start() method using a "Car" object"""

class vehicle:
    def start(self):
        print("Vehicle start class")
class Car(vehicle):
    def car_info(self):
        print("This is car class")
obj= Car()
obj.start()  # calling parent class method
    