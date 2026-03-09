# class:class is a blueprint of an object
# it defines the attributes and behaviors of an object.

# object: an instance of a class. It is a concrete entity based on the class blueprint
        # objects can have their own unique values for the attributes defined in the class.
        # through objects, we can access the attributes and methods defined in the class.
# attributes: characteristics or properties of an object

# methods: functions defined inside a class that describe the behaviors of an object

# constructor: a special method in a class that is automatically called when an object of the class is created.
            #  method name: __init__()

# instance variable: variables that are unique to each instance or object of a class

# class variable: variables that are shared among all instances of a class  

# any variable declare with self keyword is called instance variable
# any method declare with self keyword is called instance method
# example of a class and object in python
class Dog:
    # attributes// class variable// class attribute
    species = "Canis familiaris"

    # constructor
    def __init__(self, name, age):#here name and age are attributes of the class
        """
        Docstring for __init__????
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
my_dog = Dog("Tom", 5)
result = my_dog.bark()
print(result)  # because we have returned it will print first, Output: Canis familiaris says Woof!

my_dog.show_dog_name()  # Output: Dog's name is Tom
my_dog.show_dog_age()   # Output: Dog's age is 5 years

print("*"*50)
# create another class named School
class School:
    school_name = "Music School"  # class variable

    # constructor
    def __init__(self, student_name, student_rollno):
        self.Name = student_name
        self.RollNo = student_rollno

    # method // instance method
    def Standard(self):
        return f"{self.Name} is in 3rd standard"
    
     # method // instance method
    def Show_Student_Name(self):
        print(f"Student name with {self.Name}, ")

    # method // instance method
    def Show_Student_RollNo(self):
        print(f"has roll no. {self.RollNo}")

"""Why Python Doesn't Allow Multiple Constructors?
Because Python does not support method overloading like Java or C++.
If you define the same method twice, the latest one replaces the previous one.
    def __init__(self, student_address, student_phone):
        self.Address = student_address
        self.Phone = student_phone
 
    def Show_Student_Address(self):
        print(f"Student address is {self.Address}")"""

# creating an object of the School class
student1 = School("Aayush", 1)
student2 = School("Sandeep", 2)

print(f"Welcome to {School.school_name}")  # Output: Welcome to Music School

# accessing methods of the School class through the objects
student1.Show_Student_Name()  # Output: Student name is Aayush
student1.Show_Student_RollNo()  # Output: Student Roll no is 1
student2.Show_Student_Name()  # Output: Student name is Sandeep
student2.Show_Student_RollNo()  # Output: Student Roll no is 2

print(f"{student1.Name} has roll number {student1.RollNo}")
print(f"{student2.Name} has roll number {student2.RollNo}")

print("_"*50)
# creating another object of the School class
xyz = School("Rohit", 3)
xyz.Show_Student_Name()  # Output: Student name is Rohit
xyz.Show_Student_RollNo()  # Output: Student Roll no is 3

print("_"*50)
#Deepesh's code
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
