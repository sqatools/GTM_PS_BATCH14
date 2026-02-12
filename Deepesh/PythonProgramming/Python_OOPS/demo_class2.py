class Car:
    def __init__(self, car_name, car_price, car_comp):
        self.CarName = car_name
        self.CarPrice = car_price
        self.CarComp = car_comp

    def show_car_details(self):
        print("car name :", self.CarName)
        print("car price :", self.CarPrice)
        print("car company :", self.CarComp)

if __name__ == "__main__":
    obj = Car("Fortuner", "60Lac", "Toyota")
    obj.show_car_details()
    print("module name :", obj.__module__)
    print("module name:", __name__)




    


