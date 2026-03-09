# single level inheritance example in Python
class Animal:
    def speak(self):
        print("Animal speaks") 
class Dog(Animal):
    def bark(self):
        print("Dog barks") 
# creating an object of the Dog class
dog = Dog()
print(dog.speak())  # Output: Animal speaks
print(dog.bark())   # Output: Dog barks

# creating an object of the Animal class
animal = Animal()
print(animal.speak())  # Output: Animal speaks
