
class Hotel:
    def __init__(self, hotelname, hoteladdress, roomprice):
        self.hotelname = hotelname
        self.hoteladdress = hoteladdress
        self.roomprice = roomprice

    def display_info(self):
        print("Hotel Name:", self.hotelname)
        print("Hotel Address:", self.hoteladdress)
        print("Room Price:", self.roomprice)

    def calculate_stay_cost(self, num_nights):
        total_cost = self.roomprice * num_nights
        print(f"Total cost for {num_nights} nights at {self.hotelname}: ${total_cost}")
        return total_cost
    
    def apply_group_discount(self, num_rooms, discount_percent):
        total_before_discount = self.roomprice * num_rooms
        discount = total_before_discount * (discount_percent / 100)
        final_cost = total_before_discount - discount
        print(f"Group booking ({num_rooms} rooms) with {discount_percent}% discount: ${final_cost}")
        return final_cost