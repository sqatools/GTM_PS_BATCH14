class x:
    def __init__(self, a):
        self.a = a


    def display_a(self):
        print(f"Value of a is: {self.a}")


class y(x):
    def __init__(self, a, b):
        self.b = b
        super().__init__(a)


    def display_b(self):
        print(f"Value of b is: {self.b}")


obj = y(10, 20)
obj.display_a()
obj.display_b()