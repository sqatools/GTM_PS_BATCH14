

class Hotel:
    def __init__(self,name,address,room_price):
        self.name=name
        self.address=address
        self.room_price=room_price


    def hotel_details(self):
        return self.name,self.address,self.room_price

    def room_type(self):
        print("There are three tpyes of room viv. delux,superdelux and king")

    def facility(self):
        print("It provides free wifi and breakfast")

    