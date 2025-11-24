#https://sqatools.in/python-basic-programs/
##python Program to add two integer values.
#Python Program to subtract two integer values.
#Python program to multiply two numbers.
#In this Python basic program, we will repeat a given string 5 times.

# a=10
# b=10
# c=a+b
# sub=a-b
# mul=a*b
# str="soniya"
# print("print c",c)
# print("print sub",sub)
# print("print mul",mul)
# print("str*5",str*5)#In this Python basic program, we will repeat a given string 5 times.

# Python program to get the median of given numbers.
# Note: all the numbers should be arranged in ascending order
# Formula : (n+1)/2
# n = Number of values
# Input : [45, 60, 61, 66, 70, 77, 80]
# Output:  66

# values =[45, 60, 61, 66, 70, 77, 80]
# values.sort()
# n=len(values)
# print(n)
# if n%2 ==0:
#     median_value = (values[n // 2 - 1] + values[n // 2]) / 2
# else:
#     median_value = values[n // 2]
# print("the median value",median_value)


# #Python program to print the square and cube of a given number.
# num1=9
# squre=num1**2
# print(squre)
# cube=num1**3
# print(cube)

#Python program to interchange values between variables.
# a=10
# b=20
# a,b=b,a
# print("values of a",a)
# print("values of b",b)

#Python program to solve this Pythagorous theorem.
#heorem : (a2 + b2 = c2)

# a = 10
# b = 10
#
# c = (a**2 + b**2) ** 0.5
# print("The value of c is:", c)
#

#11). Python program to solve the given math formula.
# Formula : (a – b)2 = a^2 + b^2 – 2ab
# a = 2
# b = 3
# result = a**2-2*a*b+b**2
#
# print("(a-b)^2: ",result)

# 12Python program to solve the given math formula.

# a = 3
# b = 2
# result = (a+b)*(a-b)
#
# print("(a^2-b^2): ",result)

# 13). Python program to solve the given math formula.
# Formula : (a + b)3 = a3 + 3ab(a+b) + b3

# a = 3
# b = 2
# result = a**3+3*a*b*(a+b)+b**3
#
# print("(a+b)^3: ",result)
#
#
# #ython program to calculate the area of the square.
#
# side = int(input("Enter the side of a square: "))
# print("Area of sqaure: ",side**2)

# Python program to calculate the area of a circle.

# radius=int(input("enetr the radius value"))
# area=3.14*radius*radius
# print ("area of circle",area)

# Check whether the given number is an Armstrong number.
# num= a=153
#
# rev=0
# while a>0:
#     rem =a%10
#     rev=rev+rem**3
#     a=a//10
# if rev == num:
#     print("It is a armstrong number")
# else:
#     print("It is not a armstrong number")


# #21). Python program to print the current date in the given format
# Output: 2023 Jan 05
# Note: Use the DateTime library
# import datetime
# date=datetime.datetime.now()
# print (date)
# print (date.strftime( "%y %b %d"))#              need to discuss about this structure

####Python program to calculate days between 2 dates

# from datetime import date
#
# date_1 = date(2023, 1, 5)
# date_2 = date(2023, 1, 22)
#
# result = (date_2 - date_1).days
# print ("Number of Days between the given Dates are: ", result, "days")  ## need to discuss about the .days format\

#23). Python program to get the factorial of the given number.


# num = n = int(input("Enter a number: "))
# fact = 1
# while n > 0:
#     fact *= n
#     n -= 1
# print(f"Factorial of {num}: {fact}")


# import math
#
# num = int(input("Enter a number: "))
# print("Factorial of", num, "is", math.factorial(num))

#Python program to reverse a given number
# num = int(input("Enter a number: "))
#
# reverse = str(num)
#
# print("Reverse: ",reverse[::-1])


#Program to get the Fibonacci series between 0 to 50

num1 = 0
num2 = 1
count = 0

print("Sequence is: ",end=" ")#why we need "end=""
while count<50:
    print(num1,end=" ")#why we need "end=""
    n2 = num1+num2
    num1 = num2
    num2 = n2
    count += 1

#26 Python program to check given number is palindrome or not.

n = num = int(input("Enter a number: "))
rev = 0

while n>0:
    rem = n%10
    rev = rev*10+rem
    n = n//10

if num == rev:
    print("Given number is a palindrome number")
else:
    print("Given number is not a palindrome number")

