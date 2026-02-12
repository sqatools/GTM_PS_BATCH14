from Car import Car
from School import School
from ITCompany import ITCompany
from HRDepart import HRDepart
from Hotel import Hotel


class ManagementClass:
    """Orchestrator class that creates and manages all 5 classes."""
    
    def __init__(self):
        # Create objects of all 5 classes
        self.car = Car("Tesla Model 3", 50000, "Tesla")
        self.school = School("ABC School", 5000, "123 Education Lane")
        self.it_company = ITCompany("TechCorp", "456 Tech Park", "Active")
        self.hr_depart = HRDepart("John HR Manager", "Sarah Trainer", "Team Building")
        self.hotel = Hotel("Grand Plaza Hotel", "789 Main Street", 150)
    
    def manage_all_classes(self):
        """Access and demonstrate all methods from all 5 classes."""
        
        print("=" * 50)
        print("CAR MANAGEMENT")
        print("=" * 50)
        self.car.display_info()
        self.car.calculate_tax()
        self.car.apply_discount(15)
        
        print("\n" + "=" * 50)
        print("SCHOOL MANAGEMENT")
        print("=" * 50)
        self.school.display_info()
        self.school.calculate_total_fee(100)
        self.school.apply_scholarship(50, 10)
        
        print("\n" + "=" * 50)
        print("IT COMPANY MANAGEMENT")
        print("=" * 50)
        self.it_company.display_info()
        self.it_company.hire_employee("Swarna")
        self.it_company.update_status("Expanding")
        
        print("\n" + "=" * 50)
        print("HR DEPARTMENT MANAGEMENT")
        print("=" * 50)
        self.hr_depart.display_info()
        self.hr_depart.conduct_training("Engineering")
        self.hr_depart.recruitment_drive("Software Developer")
        
        print("\n" + "=" * 50)
        print("HOTEL MANAGEMENT")
        print("=" * 50)
        self.hotel.display_info()
        self.hotel.calculate_stay_cost(5)
        self.hotel.apply_group_discount(10, 20)


# Main execution
if __name__ == "__main__":
    management = ManagementClass()
    management.manage_all_classes()