from car_class import Car
from hotel_class import Hotel
from it_company_class import It_Company
from school_class import School

car_obj= Car("Kaylaq",1200000,"Skoda")
hotel_obj=Hotel("Le-Roi","Jawahar Nagar",5000)
it_company_obj=It_Company("Rakuten","Bangalore","MNC")
school_object=School("Vidya Asharam",300000,"Pratap Nagar")

car_obj.car_stop()
car_obj.car_details()
car_obj.car_start()

hotel_obj.hotel_details()
hotel_obj.room_type()
hotel_obj.facility()

it_company_obj.presence()
it_company_obj.turn_over()
it_company_obj.owner_name()

school_object.details()
school_object.rank()
school_object.standatd()