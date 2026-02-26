class Methodoverloading:

    def add(self, a, b):
        print(a+b)

    def add(self, b, c):
        print(b-c)

    def sub(self, x, y):
        print(x-y)
    def sub(self, x,y,z):
        print(x-y-z)

obj = Methodoverloading()
obj.add(100, 20)# 80
obj.add(15, 5)# 10
#obj.sub(100, 20) # This will raise an error because the second sub method overrides the first one
obj.sub(100, 20, 10) # 70

class ParentClass:

    def add(self, a , b):
        print("This is parent class method")

class ChildClass(ParentClass):
    def add(self, a, b):
        print("This is child class method")

obj2 = ChildClass()
obj2.add(10, 20) # This will call the child class method and print