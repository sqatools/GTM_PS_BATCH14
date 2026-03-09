class Hotel:
    def __init__(self, Hotelname, Hoteladdress, Roomprice):
        self.Hotelname = Hotelname
        self.Hoteladdress = Hoteladdress
        self.Roomprice = Roomprice

    def Show_Hotel_Name(self):
        print(f"Hotel name is {self.Hotelname}")    

    def Show_Hotel_Address(self):
        print(f"Hotel address is {self.Hoteladdress}")

    def Show_Room_Price(self):
        print(f"Hotel room price is {self.Roomprice}")
    