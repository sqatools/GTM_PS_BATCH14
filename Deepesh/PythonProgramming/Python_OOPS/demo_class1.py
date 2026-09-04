from demo_class2 import Car

class Showroow:
    def __init__(self):
        self.car_obj = Car("Harrier", "30 Lac", "TATA")

    def greeting(self):
        print("Welcome to car Showroom")


print("_"*50)
obj1 = Showroow()
obj1.greeting()
obj1.car_obj.show_car_details()

print("module name of showroow class :", obj1.__module__)
print("module name car class :", obj1.car_obj.__module__)

#Showroow.car_obj.show_car_details()


