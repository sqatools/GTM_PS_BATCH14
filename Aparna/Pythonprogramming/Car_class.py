class Car():
    def __init__(self, name="Honda", price="6.0L", company="Honda"):
        print("This is a car class.")
        self.name = name
        self.price = price
        self.company = company

    def displaycar_details(self):
        print(f"Car name: {self.name}, Car price: {self.price}, Car company: {self.company}")

    def starting_car(self):
        print(self.name, "is starting.")

    def stopping_car(self):
        print(self.name, "is stopped.")
        
        
#car = Car("Honda", "4.5L", "Hyndai")
#car.display_details()
#car.start_car()
#car.stop_car()