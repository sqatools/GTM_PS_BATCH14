# polymorphism in python
# polymorphism means many forms
# it allows us to define methods in the child class with the same name as defined in their parent class
# when a method in a subclass has the same name, same parameters or signature as a method in its super-class, then the method in the subclass is said to override the method in the super-class.
# polymorphism is often used in OOP to implement method overriding and operator overloading.
# there are two types of polymorphism in python
# 1. compile time polymorphism (static polymorphism)
# compile time polymorphism (static polymorphism) : it is achieved by method overloading and operator overloading.
# 2. run time polymorphism (dynamic polymorphism)
# run time polymorphism (dynamic polymorphism) : it is achieved by method overriding.

#1. method overloading : it is a feature that allows a class to have more than one method with the same name, but with different parameters.
# Python does not support method overloading by default, but we can achieve it by using default arguments or variable-length arguments.
class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c
math_obj = MathOperations()
print(math_obj.add(10, 20))        # Output: 30
print(math_obj.add(10, 20, 30))    # Output: 60

class AV:
    def add(self, *args):
        return sum(args)
av_obj = AV()
print(av_obj.add(10, 20))            # Output: 30
print(av_obj.add(10, 20, 30, 40))    # Output: 100

#2. method overriding : it is a feature that allows a subclass to provide a specific implementation of a method that is already defined in its superclass.
class Animal:
    def sound(self):
        return "Animal makes a sound"
class Dog(Animal):
    def sound(self):
        return "Dog barks"
class Cat(Animal):
    def sound(self):
        return "Cat meows"
animal_obj = Animal()
dog_obj = Dog()
cat_obj = Cat()
print(animal_obj.sound())  # Output: Animal makes a sound
print(dog_obj.sound())     # Output: Dog barks
print(cat_obj.sound())     # Output: Cat meows




#3. operator overloading : it is a feature that allows us to define custom behavior for operators in our classes.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # overloading the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def display(self):
        return f"Point({self.x}, {self.y})"
point1 = Point(2, 3)
point2 = Point(4, 5)
point3 = point1 + point2  # using overloaded + operator
print(point3.display())    # Output: Point(6, 8)

