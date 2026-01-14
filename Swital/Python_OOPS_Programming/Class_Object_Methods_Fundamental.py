# class : blueprint or template for creating objects
# Object : instance of a class
# method : function defined inside a class
# instance variable : variable that is unique to each instance of a class
# class variable : variable that is shared among all instances of a class
# constructor : special method that is called when an object of the class is created
"""
# instance method:
A method that is bound to the instance of the class.
    It takes 'self' as the first parameter and can access instance variables and other instance methods.
"""
class abc:
    def __init__(self):
        pass
    def instance_method(self):
        return "This is an instance method"
# creating an object of the abc class
obj = abc()
print(obj.instance_method())  # Output: This is an instance method

class Dog:
    # class variable
    species = "Canis familiaris" #species is class variable

    # constructor
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable

    # instance method
    def bark(self):
        return f"{self.species} says Woof!"
dog_obj = Dog("Buddy", 3)
print(dog_obj.bark())  # Output: Canis familiaris says Woof!

"""
# class method:
A method that is bound to the class and not the instance of the class.  
It takes 'cls' as the first parameter and can access class variables and other class methods.
"""
class Circle:
    # class variable
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius  # instance variable
    
    # class method
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
# creating an object of the Circle class using class method
circle_obj = Circle.from_diameter(10)
print(f"Radius of circle with diameter 10: {circle_obj.radius}")  # Output: Radius of circle with diameter 10: 5.0
