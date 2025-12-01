"""
marks = input("enter the Mrks : ")
x = int(marks)
if x <= 30:
    print("Failed")
else:
    print("passed")

print("*"*50)
"""
""""
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

print("*"*50)
"""
"""
# 4). Python program to check the given number divided by 3 and 5.

num = input("Enter your number: ")
x = int(num)

if x % 3 == 0 and x % 5 == 0:
    print("number divisible by 3 and 5")
else:
    print("number not divisible by 3 and 5")
 """"""""
# 5). Python program to print the square of the number if it is divided by 11
num = input("enter your number")
y = int(num)
if y % 11 == 0:
    square = y * y
    print("square of the number :", square)
else:
    print("ths number not divisible by 11")

#7). Python program to check given number is odd or even.

num = input("enter number: ")
x = int(num)
if x % 2 == 0:
    print ("Even Number")
else:
    print("number is odd")
"""
"""
#Check a number is part of the Fibonacci series

fibnumbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
x = input("enter any number between 1 to 30: ")
num = int(x)

if num  in fibnumbers:
    print("number is fib number")
else:
    print("number is not a Fib number")
# Python program to check authentication with the given username and password.
"""
"""
username = "nalini"
pwd = "123456"
uname = input("enter username:")
password = input("enter Password")
if uname == username and password == pwd:
    print("valid user")
else:
    print("invalid user")
"""






