"""
1. single inheritance : when one class inherits from another class then it is called single inheritance.
                        class A --> class B
2. multi-level inheritance :  when a class inherits from a derived class then it is called multi-level inheritance.
                      class A --> class B --> class C
3. multiple inheritance : when a class inherits from more than one class then it is called multiple inheritance.
                      class A --> class C  , class B --> class C
"""

# multiplevel inheritance
class grandParent:
    def __init__(self, grand_name):
        self.grand_name = grand_name  # instance variable
    
    def grandparent_method(self):
        print("This is grandparent method")

    def show_grandparent_info(self):
        print(f"Grandparent Name: {self.grand_name}")

class Parent(grandParent):
    # parent class constructor
    def __init__(self, parent_name, parent_business, grand_name):
        self.parent_name = parent_name # instance variable
        self.parent_business = parent_business  # instance variable
        super().__init__(grand_name)  # calling grandparent class constructor
        
    
    def parent_method(self):
        print("This is parent method") 

    def show_parent_info(self):
        print(f"Parent Name: {self.parent_name}, Business: {self.parent_business}")

# child class inheriting from parent class
class Child(Parent):
    def __init__(self, child_name, child_age, p_name, p_business, grand_name):
        self.child_name = child_name # instance variable
        self.child_age = child_age # instance variable
        # calling parent class constructor in child class
        super().__init__(p_name, p_business, grand_name)

        # calling parent class constructor
    def child_method(self):
        print("This is child method")

    def show_child_info(self):
        print(f"Child Name: {self.child_name}, Age: {self.child_age}")


# creating an object of Child class
user_name = "Rajesh"
user_business = "Software"
child_obj = Child(child_name="Deepesh", child_age=25, p_name=user_name, p_business=user_business, grand_name="Mohar")
child_obj.parent_method()  # calling parent class method
child_obj.child_method()   # calling child class method

child_obj.show_parent_info()  # showing parent info
child_obj.show_child_info()   # showing child info
child_obj.grandparent_method()  # calling grandparent class method

