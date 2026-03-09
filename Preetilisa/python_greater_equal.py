marks = int(input("Please enter your marks:"))

if marks <= 30:
    print("Failed in Exam")
elif 30 < marks <= 40:   # chain action logic
    print("Pass with 3rd grade")
elif marks > 40 and marks <= 60:
    print("Pass with 2nd grade")
elif marks > 60 and marks <= 80:
    print("Pass with 1st Grade")
elif marks > 80 and marks <= 100:
    print("Pass with A++ Grade")
elif marks > 100 and marks <= 150:
    print("Pass with O++ Grade")
else:
    print("Marks should be less than 200")
