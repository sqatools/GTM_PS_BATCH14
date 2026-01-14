"""
1. single inheritance : when one class inherits from another class then it is called single inheritance.
                        class A --> class B
2. multi-level inheritance :  when a class inherits from a derived class then it is called multi-level inheritance.
                      class A --> class B --> class C
3. multiple inheritance : when a class inherits from more than one class then it is called multiple inheritance.
                      class A --> class C  , class B --> class C

4. Hirachy inheritance : when a class inherits from a base class and other class also inherits from the same base class then it is called hirarchy inheritance.
                      class A --> class B  , class A --> class C
"""

# multiple inheritance
class Developer:
    def developer_method(self):
        print("This is developer method")

class Tester:
    def tester_method(self):
        print("This is tester method")  
    
class Manager:
    def manager_method(self):
        print("This is manager method")


# Child class inheriting from Developer and Tester class
class ITEmployee(Developer, Tester, Manager):
    def it_employee_method(self):
        print("This is IT Employee method")



obj = ITEmployee()
obj.developer_method()  # calling developer class method
obj.tester_method()     # calling tester class method   
obj.it_employee_method()   # calling IT Employee class method
obj.manager_method()    # calling manager class method