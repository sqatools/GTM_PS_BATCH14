class Car:

    # Constructor
    def __init__(self, name, price, company):
        self.name = name
        self.price = price
        self.company = company

    def display_details(self):
        print("Car Name:", self.name)
        print("Price:", self.price)
        print("Company:", self.company)

    def start_car(self):
        print(self.name, "is starting...")

    def stop_car(self):
        print(self.name, "is stopping...")

car1 = Car("Honda", "4.5L", "Hyndai")
car1.display_details()
car1.start_car()
car1.stop_car()
