class school:
    school_name = "ABC High School"

    #constructor
    def __init__(self, student_name, student_age):
        print(f"Welcome to {self.school_name}")
        self.name = student_name  # instance variable
        self.age = student_age    # instance variable
    
    @classmethod
    def get_school_name(cls):
        return cls.school_name
    
    def show_the_student_name(self):
        print(f"Student's name is {self.name}")
school1 = school("Jayanthi", 16)
print(school1.get_school_name())
print(school.get_school_name(school))
school1.show_the_student_name()
school1.show_the_student_name(school1)
