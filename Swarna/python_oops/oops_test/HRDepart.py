class HRDepart:
    def __init__(self, recruitment, training, activity):
        self.recruitment = recruitment
        self.training = training
        self.activity = activity

    def display_info(self):
        print("Recruitment:", self.recruitment)
        print("Training:", self.training)
        print("Activity:", self.activity)
    
    def conduct_training(self, department_name):
        print(f"Training session conducted for {department_name} department")
    
    def recruitment_drive(self, position):
        print(f"Recruitment drive started for {position}")