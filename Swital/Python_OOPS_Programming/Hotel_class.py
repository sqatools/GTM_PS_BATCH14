class Hotel:

    def display_details(self):
        print("Hotel Name:", self.hotelname)
        print("Hotel Address:", self.hoteladdress)
        print("Room Price:", self.roomprice)

    def book_room(self):
        print("Room booked at", self.hotelname)

    def cancel_booking(self):
        print("Booking cancelled at", self.hotelname)


h1 = Hotel()
#h1.display_details() 
h1.hotelname = "Taj Hotel"
h1.hoteladdress = "Mumbai"
h1.roomprice = 5000

h1.display_details()
h1.book_room()
h1.cancel_booking()
