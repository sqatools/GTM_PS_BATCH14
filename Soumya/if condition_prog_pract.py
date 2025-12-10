"""
1). Python program to check given number is divided by 3 or not.
"""

"""print("*"*50)
num1 = int(input("enter the number"))
if num1%3==0 :
    print("given number is divisible by 3")
else :
    print("given number is not divisible by 3")
    
"""

"""
2). If else program to get all the numbers divided by 3 from 1 to 30.
"""
for num2 in range(1,30) :
    if num2%3==0:
        print(num2)

"""
3). If else program to assign grades as per total marks.
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marksProgramming fundamentals book
"""

"""
print("*"*50)
marks = int(input("enter the number"))
if marks <40 :
    print("Failed")
elif marks >=40 and marks <=50:
    print("grade C")
elif marks >50 and marks <=60:
    print("grade B")
elif marks >60 and marks <=70:
    print("grade A")
elif marks >70 and marks <=80:
    print("grade A+")
elif marks >80 and marks <=90:
    print("grade A++")
elif marks >90 and marks <=100:
    print("grade Excellent")
else :
    print("invalid marks")

"""
"""
4). Python program to check the given number divided by 3 and 5.

num2 = int(input("enter the number"))
if num2%3==0 and num2%5==0 :
    print("given number is divisible by 3 and 5")
else :
    print("given number is not divisible by 3 and 5")
"""

"""
5). Python program to print the square of the number if it is divided by 11.

num3 = int(input("enter the number"))
if num3%11==0 :
    print(num3**2)
else :
    print("given number is not divisible by 11")
"""

"""
6). Python program to check given number is a prime number or not.

num4 = int(input("enter the number"))
for i in range(2, num4) :
    count = 0
    if num4%i==0:
        count += 1
if count>0 :
        print("not a prime number")
else :
        print("prime number")
"""

"""
7). Python program to check given number is odd or even.

num5 = int(input("enter the number"))
if num5%2==0 :
    print("given number is even number")
else :
    print("given number is odd number")
"""

"""
8). Python program to check a given number is part of the Fibonacci series from 1 to 10.
fib = [1,1,2,3,5,8,13,21,34,55,89]
num6 = int(input("enter the number"))
if num6 in fib:
    print("given number is fib number")
else :
    print("given number is not fib number")
"""

"""
9). Python program to check authentication with the given username and password.

username = str(input("enter the username"))
password = str(input("enter the password"))
if username == password :
    print("login successful")
else :
    print("login failed")
"""

"""
10). Python program to validate user_id in the list of user_ids.
uid_list = [1, 2, 4, 6]
id = int(input("enter the user id"))
if id in uid_list:
    print("user id is valid")
else :
    print("user id is not valid")
    
"""

"""
11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.

num7 = int(input("enter the number"))
if num7%2==0 or num7%3==0 :
    print("given number is divisible by 2 or 3")
    print(num7**2)
else :
    print("given number is not divisible by 2 0r 3")
"""

"""
12). Python program to check given number is divisible by 3 or not.

round1 = str(input("Enter round1 result:"))
round2 = str(input("Enter round2 result:"))


if round1 == "passed":
    print("Congrats your 1st round is clear")
    if round2 == "passed":
        print("Congrats 2nd round is clear, you are placed")
    else:
        print("Failed in 2nd round, please try next time")
else:
    print("Failed in 1st round, please try next time")

"""

"""
13). Python program to determine whether a given number is available in the list of numbers or not.

num8 = int(input("Given number is"))
list8 = [1, 3, 5, 6, 7]
if num8 in list8 :
    print(f"{num8} is available IN LIST")
else:
    print(f"{num8} is not available IN LIST")
"""

"""
14). Python program to find the largest number among three numbers.

n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
n3=int(input("enter the third number"))
if n1>n2 and n1>n3 :
    print(f"{n1} is the largest number among three numbers")
elif n2>n1 and n2>n3 :
    print(f"{n2} is the largest number among three numbers")
elif n3>n1 and n3>n2 :
    print(f"{n3} is the largest number among three numbers")
    
"""

"""
15). Python program to check any person eligible to vote or not
age > 18+ : eligible
age < 18: not eligible


age = int(input("enter the age"))
if age>18 :
    print("age",age, "is eligible to vote")
else :
    print("age", age, "is not eligible to vote")
"""

"""
18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
Input = Enter marks: 45
Output = Pass

num9 = int(input("enter the student marks"))
if num9>=35 :
    print("student passed the exam")
else :
    print("student failed the exam")

"""

"""
16). Python program to check whether any given number is a palindrome.
Input: 121
Output: palindrome

num10 = 101
num11= str(num10)

if num10 == int(num11[::-1]) :
    print("given number is palindrome")
else :
    print("given number is not palindrome")
"""

"""
17). Python program to check if any given string is palindrome or not.
Input: ‘jaj’
output = palindrome

str1 = "jaji"
str2 = str1[::-1]
if str1==str2 :
    print("given string is palindrome")
else :
    print("given str is not palindrome")
"""

"""
19). Python program to check whether the given number is positive or not.
Input = 20 
Output = True

p1 = int(input("enter the first number"))
if p1>0 :
    print("true")
else :
    print("false")
"""


"""
21). Python program to check whether the given number is positive or negative and even or odd.
Input = 26
Output = The given number is positive and even


p2 = int(input("enter the number"))
if p2>0 :
     if p2%2==0 :
         print("given number is positive and even number")
     else :
         print("given number positive and odd number")
else:
     if p2%2==0 :
        print("given number is negative and even number")
     else :
        print("given number is negative and odd number")
"""


"""
22). Python program to print the largest number from two numbers.
Input:
25, 63
Output = 63

p3 = 89
p4 = 63
if p3>p4 :
    print(f"{p3} is the largest number from two numbers")
else :
    print(f"{p4} is the largest number from two numbers")
"""

"""
23). Python program to check whether a given character is uppercase or not.
Input = A
Output = The given character is an Uppercase

char1 = input("enter the character")
if char1.isupper() :
    print(f"{char1} is uppercase")
else :
    print(f"{char1} is lowercase")
"""

"""
25)Python program to check whether the given character is lowercase or not.
Input = c
Output = True

char2 = input(" enter the character")
if char2.islower():
    print(f"{char2} is lowercase")
else :
    print(f"{char2} is uppercase")
"""

"""
25). Python program to check whether the given number is an integer or not.
Input = 54
Output = True

num54 = 54
if type(num54)==int :
    print(f"{num54} is an integer")
else :
    print(f"{num54} is not an integer")
"""

""""
26). Python program to check whether the given number is float or not.
Input = 12.6
Output = True

f1 = 12.6
if type(f1)==float :
    print("true")
else :
    print("false")

"""


"""
27). Python program to check whether the given input is a string or not.
Input = ‘sqatools’
Output = True

str2 = 'sqatools'
if type(str2)==str :
    print("true")
else :
    print("false")

"""

"""
28). Python program to print all the numbers from 10-15 except 13
Output:
10
11
12
14

print(""*30)
for i in range(10,16):
    if i!=13:
        print(i)
"""


"""
Leap year or not 

year = int(input("Enter the year: "))

if (year%100 != 0 or year%400 == 0) and year%4 == 0:
    print("The given year is leap year.")
else:
    print("The given year is not leap year.")
"""


"""
Pattern program

for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")

    print()
"""
"""
patern program 2nd

for i in range(1,6):
    for j in range(1,7-i):
        print("*", end=" ")

    print()
"""

"""
program pattern 3 

for i in range(7):
    if i==0 or i==6:
        print("  * * *")
    else :
        print("*" + " " * 7 + "*")
"""

"""
program pattern 4

for i in range(1, 6):
    for j in range(1, 6):
        print("*", end=" ")
    print()
"""


for i in range(1, 6):
    if i == 1 or i ==5:
        print("  * * *")
    else :
        print("*", "*", "*", "*", "*")




    





























