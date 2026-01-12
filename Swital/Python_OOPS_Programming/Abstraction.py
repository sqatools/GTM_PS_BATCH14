# Abstraction : It is the process of hiding the complex implementation details and showing only the essential features of the object.
from abc import ABC, abstractmethod
# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
# Dog class inheriting from Animal abstract class
class Dog(Animal):
    def sound(self):
        return "Woof Woof"
# Cat class inheriting from Animal abstract class
class Cat(Animal):
    def sound(self):
        return "Meow Meow"
# creating objects of Dog and Cat classes
dog = Dog()
cat = Cat()
print(dog.sound())  # Output: Woof Woof
print(cat.sound())  # Output: Meow Meow
# trying to create an object of the abstract class will raise an error
# animal = Animal()  # This will raise TypeError: Can't instantiate abstract class Animal with abstract methods sound
# The abstract class Animal cannot be instantiated directly.
# It can only be used as a base class for other classes that implement the abstract methods.
# This ensures that any subclass of Animal must provide an implementation for the sound() method.
# Abstraction helps in reducing complexity and increases efficiency by allowing the user to focus on interactions at a higher level.
# It also helps in achieving security by restricting access to certain details of the implementation.
