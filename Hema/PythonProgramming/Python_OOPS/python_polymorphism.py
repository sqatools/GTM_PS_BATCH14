# polymorphism in Python
# Polymorphism allows methods to do different things based on the object it is 
# acting upon.
"""
method overloading and method overriding are two types of polymorphism in Python.
1. Method Overloading:
   - Method overloading is a feature that allows a class to have more than one
     method with the same name, but different parameters (different type or number of parameters).
   - Python does not support method overloading directly.
2. Method Overriding:
   - Method overriding is a feature that allows a subclass to provide a specific 
     with same method in parent class and child class, child class method overrides
        the parent class method.  
"""

# Method Overloading Example
class MathOperations:
    def add(self, a, b, c=5):
        return a + b + c
    
    def add(self, p, q):
        return p + q
    
math = MathOperations()
#print(math.add(10, 20))

#print(math.add(10, 20, 30)) 
# This will raise an error because the second add method overrides the first one
# print(math.add(10, 20, 30))

# Method Overriding Example: In this case if child and parent class have same method 
# name, and there inhetnace relationship between them, then child class method overrides
# the parent class method.

class Parent:
    def greet(self):
        return "Hello from Parent"
    
    def add(self, x, y):
        return x + y
    

    def multiply(self, x, y):
        return x * y
    
class Child(Parent):
    def greet(self):
        return "Hello from Child"
    

    def add(self, x, y, z):
        return x + y + z    
    

child = Child()
print(child.greet())  # Output: Hello from Child

#print(child.add(10, 20))  # Output: 60

print(child.multiply(5, 4))  # Output: 20


