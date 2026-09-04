# Multi level inheritance in Python : it is a type of inheritance where a class (child class) inherits from another class (parent class), which in turn inherits from another class (grandparent class).
# Here, the child class inherits properties and behaviors from both the parent and grandparent classes.
# child inherits from parent, and parent inherits from grandparent.
class Grandparent:
    def grandparent_method(self):
        print("This is a method from Grandparent class") 
class Parent(Grandparent):
    def parent_method(self):
        print("This is a method from Parent class")
class Child(Parent):
    def child_method(self):
        print("This is a method from Child class")
# creating an object of the Child class
child_obj = Child() 
print(child_obj.grandparent_method())  # Output: This is a method from Grandparent class
print(child_obj.parent_method())       # Output: This is a method from Parent class
print(child_obj.child_method())        # Output: This is a method from Child class

# creating an object of the Parent class
parent_obj = Parent()
print(parent_obj.grandparent_method())  # Output: This is a method from Grandparent class
print(parent_obj.parent_method())       # Output: This is a method from Parent class

# creating an object of the Grandparent class
grandparent_obj = Grandparent()
print(grandparent_obj.grandparent_method())  # Output: This is a method from Grandparent class