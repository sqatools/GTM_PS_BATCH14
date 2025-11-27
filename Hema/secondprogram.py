# write a python program to check the given number is divisible by 3 and 5

number1 = int(input("Enter the vale: "))
if number1 % 3 == 0 and number1 % 5 == 0:
    print("The number is divisible by 3 and 5", number1)
else:
    print("The number is not divisible by 3 and 5", number1)

number1 = int(input("Enter the vale: "))
if number1 % 3 == 0 or number1 % 5 == 0:
    print("The number is divisible by 3 and 5", number1)
else:
    print("The number is not divisible by 3 and 5", number1)

##########################
#write a program to accept the student marks and provide it's result as per the marks obtained

marks= int(input("Enter the marks: "))
if marks < 35:
    print("failed in exam", marks)
elif marks > 35 and marks <= 50:
    print("Pass with 3rd grade", marks)
elif marks > 50 and marks <= 60:
    print("Pass with 2nd grade", marks)
elif marks > 60 and marks <= 75:
    print("Pass with 1st grade", marks)
elif marks > 75 and marks <= 100:
    print("Distinction", marks)
else:
    print("Marks should be less than 100", marks)