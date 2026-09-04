"""
1. single inheritance : when one class inherits from another class then it is called single inheritance.
                        class A --> class B
2. multi-level inheritance :  when a class inherits from a derived class then it is called multi-level inheritance.
                      class A --> class B --> class C
3. multiple inheritance : when a class inherits from more than one class then it is called multiple inheritance.
                      class A --> class C  , class B --> class C
"""

# multiple inheritance
class Father:
    def father_method(self):
        print("This is father method")

    
class Mother:
    def mother_method(self):
        print("This is mother method")

class Brother:
    def brother_method(self):
        print("This is brother method")


# Child class inheriting from Father and Mother class
class Child(Father, Mother, Brother):
    def child_method(self):
        print("This is child method")


# creating an object of Child class
child_obj = Child()
child_obj.father_method()  # calling father class method
child_obj.mother_method()  # calling mother class method
child_obj.child_method()   # calling child class method
child_obj.brother_method()  # calling brother class method