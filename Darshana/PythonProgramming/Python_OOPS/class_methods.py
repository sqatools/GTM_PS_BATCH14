"""
This module demonstrates the use of class methods in Python OOP.
# instance method:
A method that operates on an instance of the class. 
It takes 'self' as the first parameter and can access instance variables and other instance methods.

# classmethod:
A method that is bound to the class and not the instance of the class. It takes 'cls' as 
the first parameter and can access class variables and other class methods.

# staticmethod:
A method that does not take 'self' or 'cls' as the first parameter. 
It behaves like a regular function but belongs to the class's namespace.

"""

# Example of class methods and static methods in Python
class Circle:
    # class variable
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius  # instance variable

    # instance method
    def area(self):
        return Circle.pi * (self.radius ** 2)

    # class method
    @classmethod
    def from_diameter(cls, diameter):
        return cls.pi *2*(diameter / 2)

    # static method
    @staticmethod
    def circumference(radius, pi):
        return 2 * pi* radius   


# creating an object of the Circle class
"""
my_circle = Circle(5)
output = my_circle.area()  # Output: 78.53975
print(f"Area of circle with radius 5: {output}")

output2 = my_circle.from_diameter(10)  # Output: 31.4159
print(f"Area of circle with diameter 10: {output2}")


output3 = my_circle.circumference(5, 3.14159)  # Output: 31.4159
print(f"Circumference of circle with radius 5: {output3}")
"""

# access instance method using class name without creating object
#output = Circle.area()  # Output: 78.53975
#print(f"Area of circle with radius 5: {output}")
# TypeError: Circle.area() missing 1 required positional argument: 'self'

# access class method using class name without creating object
output2 = Circle.from_diameter(10)  # Output: 31.4159
print( f"Area of circle with diameter 10: {output2}")

# access static method using class name without creating object
output3 = Circle.circumference(5, 3.14159)  # Output: 31.4159
print(f"Circumference of circle with radius 5: {output3}")