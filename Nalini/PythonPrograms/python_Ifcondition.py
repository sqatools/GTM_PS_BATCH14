marks = input("enter the Mrks : ")
x = int(marks)
if x <= 30:
    print("Failed")
else:
    print("passed")
print("*"*50)
"""
3). If else program to assign grades as per total marks.
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks
"""
x = input("enter your Marks : ")
marks = int(x)
if marks < 40:
    print("you are failed")
elif 40 < marks < 50:
    print("grade c")
elif marks < 50 or marks < 60:
    print("grade B")
elif marks < 60 or marks < 70:
    print("grade A")
elif marks < 70 or marks < 80:
    print("grade A+")
elif marks < 80 or  marks < 90:
    print("grade A++")
elif marks < 90 or  marks < 100:
    print("Excellent")
elif marks > 100:
    print ("marks should not be more than 100")


