class HRDepartment:
    def __init__(self, recruirment, training, activity):
        self.recruirment = recruirment
        self.training = training
        self.activity = activity

    def Show_Recruitment(self):
        print(f"HR Department is responsible for {self.recruirment}")

    def Show_Training(self):
        print(f"HR Department is responsible for {self.training}")

    def Show_Activity(self):
        print(f"HR Department is responsible for {self.activity}")
