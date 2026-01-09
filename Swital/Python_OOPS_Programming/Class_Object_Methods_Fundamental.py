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