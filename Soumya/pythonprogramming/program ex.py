#Write a Python program to check whether a number is even or odd.
"""

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("even")
else:
    print("odd")

"""

#Program to Find Largest of Two Numbers
"""
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
if num1>num2:
    print("num1 is the largest number")
else:
    print("num2 is the largest number")

"""
#3. Program to Check Prime Number
"""
num1=int(input("Enter a number: "))
count = 0
for i in range(2,num1):
    if num1%i==0:
        count=count+1
if count>0:
    print(num1, "is nOt a prime number")
else:
    print(num1, "is a prime number")
"""


