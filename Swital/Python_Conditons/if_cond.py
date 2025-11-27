print("#" * 10, "Score Equality", "#" * 10)
score_s1 = 40
score_s2 = 50

if score_s1 == score_s2:
    print("score are equal")
else:
    print("score are different")

print("#" * 10, "Check Eligibility", "#" * 10)
age = 27
experience = 3

if age >= 18 and experience >= 2:
    print("Eligible for the job")
elif age >= 18 and experience < 2:
    print("Need more experience")
else:
    print("Not eligible for the job")

print("#" * 10, "Check Equal number", "#" * 10)
s1 = 10
s2 = 20
s3 = 30
s4 = 10
if s1 == s2:
    print("s1 and s2 are equal")
elif s1 == s3:
    print("s1 and s3 are equal")
elif s1 == s4:
    print("s1 and s4 are equal")
else:
    print("All are different")

print("#" * 10, "Marks which is equal and grade", "#" * 10)
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

print("#" * 10, "Withdraw nested if condition", "#" * 10)
balance = 5000
withdraw = 3000
pin = 1234

if pin == 1234:
    if withdraw <= balance:
        print("Withdrawal successful")
    else:
        print("Insufficient balance")
else:
    print("Incorrect PIN")

print("#" * 50)
# write a python program to check the given number is divisible by 2 and 7 using AND
num = int(input("Enter number:"))
a = int(num)
if a % 2 == 0 and a % 7 == 0:
    print("number is divisible by both the value")
else:
    print("number is not divisible by both the value")

# write a python program to check the given number is divisible by 2 and 7 using OR
print("#" * 50)
num = int(input("Enter number:"))
a = int(num)
if a % 2 == 0 or a % 7 == 0:
    print("number is divisible by both the value")
else:
    print("number is not divisible by both the value")

# write a program to accept the student marks and provides its result as marks obtained.
print("#" * 50)
mark = int(input("Enter Mark: "))
if mark <= 35:
    print("Failed")
elif 35 < mark <= 60:
    print("Grade D")
elif 60 < mark <= 70:
    print("Grade C")
elif 70 < mark <= 80:
    print("Grade B")
elif 80 < mark <= 99:
    print("Grade A")
else:
    print("Mark should be less than 100")

# write a python program to check given value is available in list of values.
print("#"*50)
list1 = [2, 4, 6]
val = 3
if val in list1:
    print("value is in list")
else:
    print("value is not in list")
