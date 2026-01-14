# Multiple level inheritance in Python using parent-child-grandchild relationship:
# Here child inherit from multiple parents 
class Father:
    def father_method(self):
        print("This is father method")
    def show_father_info(self, father_name):
        print(f"Father Name: {father_name}")    
class Mother:
    def mother_method(self):
        print("This is mother method")
    def show_mother_info(self, mother_name):
        print(f"Mother Name: {mother_name}")
# Child class inheriting from both Father and Mother classes
class Child(Father, Mother):
    def child_method(self):
        print("This is child method")
    def show_child_info(self, child_name):
        print(f"Child Name: {child_name}")
# creating an object of Child class
child_obj = Child()
child_obj.father_method()  # calling father class method
child_obj.mother_method()  # calling mother class method
child_obj.child_method()   # calling child class method
child_obj.show_father_info("John")  # showing father info
child_obj.show_mother_info("Jane")  # showing mother info
child_obj.show_child_info("Alice")   # showing child info
