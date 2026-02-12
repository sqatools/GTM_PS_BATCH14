from Car_class import Car
from ITCompany_class import ITCompany
from School_class import School
from HRDepart_class import HRDepart
from Hotel_class import Hotel


print("#"*100)
car_m = Car("i20", "4lakh", "Hyundai")
car_m.display_details()

print("#"*100)
school_m = School("GNFC", 12343, "Pune")
school_m.school_faculty()
school_m.display_schooldata()

print("#"*100)
itcomp_m = ITCompany("Bank of america", "Ahmedabad", "Active", "9:30Am", "5:00Pm")
itcomp_m.company_starttime()
itcomp_m.data_shown()

print("#"*100)
hrd_m = HRDepart("Interview process start with hrround", "Technical", "chess")
hrd_m.details_hr()
hrd_m.activity_details()