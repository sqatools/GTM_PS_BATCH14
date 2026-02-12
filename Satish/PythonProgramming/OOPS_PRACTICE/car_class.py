

class Car:
    def __init__(self,name,price,company):
        self.name=name
        self.price=price
        self.company=company

    def car_start(self):
        print("car started")

    def car_stop(self):
        print("car stopped")

    def car_details(self):
        return self.name,self.price,self.company
