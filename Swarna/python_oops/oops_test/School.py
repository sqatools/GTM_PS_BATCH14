class School:
    def __init__(self, name, fee, address):
        self.name = name
        self.fee = fee
        self.address = address

    def display_info(self):
        print("School Name:", self.name)
        print("Fee:", self.fee)
        print("Address:", self.address)
    
    def calculate_total_fee(self, num_students):
        total = self.fee * num_students
        print(f"Total fee for {num_students} students: ${total}")
        return total
    
    def apply_scholarship(self, student_count, scholarship_percent):
        discount_per_student = self.fee * (scholarship_percent / 100)
        total_discount = discount_per_student * student_count
        print(f"Total scholarship for {student_count} students ({scholarship_percent}%): ${total_discount}")
        return total_discount