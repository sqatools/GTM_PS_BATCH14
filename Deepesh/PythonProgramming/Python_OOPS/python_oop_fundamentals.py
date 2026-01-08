# class : class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
# object : an instance of a class. It is a concrete entity based on the class blueprint.
           # objects can have their own unique values for the attributes defined in the class.
           # through objects, we can access the attributes and methods defined in the class.

# attributes : characteristics or properties of an object.
# methods : functions defined inside a class that describe the behaviors of an object.

# constructor : a special method in a class that is automatically called when an object of the class is created.
#               method name : __init__()

# instance variable : variables that are unique to each instance or object of a class.
# class variable : variables that are shared among all instances of a class.

# Example of a class and object in Python
class Dog:
    # attributes// class variable// class attribute
    species = "Canis familiaris"

    # constructor
    def __init__(self, name, age):
        """
        Docstring for __init__
        
        :param self: instance of the class
        :param name: attribute of Dog class
        :param age: atribute of Dog class
        """
        print("Welcome to Dog Family")
        self.name_value = name  # instance variable
        self.age_value = age    # instance variable

    

    # method // instance method
    def bark(self):
        return f"{self.species} says Woof!"
    
    # instance method to show dog's name
    def show_dog_name(self):
        print(f"Dog's name is {self.name_value}")


    def show_dog_age(self):
        print(f"Dog's age is {self.age_value} years")
    
# creating an object of the Dog class
my_dog = Dog("Buddy", 3)
result = my_dog.bark()
print(result)  # Output: Canis familiaris says Woof!

my_dog.show_dog_name()  # Output: Dog's name is Buddy
my_dog.show_dog_age()   # Output: Dog's age is 3 years




# any variable declare with self keyword is called instance variable
# any method declare with self keyword is called instance method
class Animal:
    def __init__(self, voice):
        print("Hello good morning")
        self.animal_name = "Lion" # instance variable
        self.animal_voice = voice  # instance variable

    # instance method
    def make_sound(self):
        print(self.animal_name)

    def show_animal_voice(self):
        print(self.animal_voice)

print("_"*50)
# creating an object of the Animal class
my_animal = Animal("Roar")
my_animal.make_sound()
my_animal.show_animal_voice()