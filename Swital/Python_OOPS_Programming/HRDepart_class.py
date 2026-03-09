class HRDepart:
    def __init__(self, recruirment, training, activity):
        self.hrrecruit = recruirment
        self.training = training
        self.act = activity
    def details_hr(self):
        print("Recruitment process are", self.hrrecruit)
        print("Training process are for", self.training)
        print("Activity are for", self.act)
    
    def activity_details(self):
        print(self.act, "for fun")
        print(self.act, "for health")

    def recuitment_details(self):
        print(self.hrrecruit, "employement")

hrd = HRDepart("3 interview scheduled", "skill upgrade", "Tennis, Badminton")
hrd.details_hr()
hrd.activity_details()
hrd.recuitment_details()

