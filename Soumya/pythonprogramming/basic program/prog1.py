# 1). Python Program to add two integer values.

num1 = 10
num2 = 20
print("addition of 2 number is:", num1+num2)
print("subtraction of 2 num is:", num1-num2)
print("multiplication of 2 num is:", num1*num2)

#4). Python program to repeat a given string 5 times.
print("_"*40)
str1 = "SQATools"
print("repeate the given string:", str1*5)

#5). Python program to get the Average of given numbers.

print("_"*40)
a = 10
b = 30
c = 40
print("average of given numbers are:", a+b+c/3)

#6). Python program to get the median of given numbers.

print("_"*40)
values = [10,60, 90, 30, 40, 50]
values.sort()
n=len(values)
if n%2==1:
    median_values=values[n//2]
else:
    median_values=(values[n//2-1] + values[n//2])/2
print(median_values)

#7) Python program to print the square and cube of a given number
print("_"*40)
num5 = 3
print("square of numbers is:", num5**2)
print("square of numbers is:", num5**3)

#8). Python program to interchange values between variables.
print("_"*40)
a=10
b=30
a,b=b,a
print("interchange value for a:", a)
print("interchange value for b:", b)

#1). Python program to check given number is divided by 3 or not.

"""
print("_"*40)
num4 = int(input("Enter a number: "))
if num4%3==0:
    print("given number is divisible by 3")
else:
    print("given number is not divisible by 3")
"""

"""
#2)If else program to get all the numbers divided by 3 from 1 to 30.

for i in range(1,31):
    if i%3==0:
        print(i, end=" ")
    else:
        continue
"""

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

marks = int(input("Enter marks: "))
if marks < 40 :
    print("fail")
elif marks >=40 and marks<50 :
    print("grade C")
elif marks >=50 and marks<60 :
    print("grade B")
elif marks >=60 and marks<70 :
    print("grade A")
elif marks >=70 and marks<80 :
    print("grade A+")
elif marks >=80 and marks<90 :
    print("grade A++")
elif marks >=90 and marks<100 :
    print("grade Excellent")
elif marks >100 :
    print("Invalid marks")
"""

"""
4). Python program to check the given number divided by 3 and 5.

num7 = int(input("Enter a number: "))
if num7%3==0 and num7%5==0:
    print("number is divisible by both 3 and 5")
else :
    print("number is not divisible by both 3 and 5")
"""

"""
5). Python program to print the square of the number if it is divided by 11.

num7 = int(input("Enter a number: "))
if num7%11==0:
    print("square of the given number is ", num7**2)
else :
    print("number is not divisible by 11")
"""


"""
6). Python program to check given number is a prime number or not.

num8 = int(input("Enter a number: "))
count = 0
for i in range(2, num8):
    if num8%i==0:
        count = count + 1
if count>0:
    print("not a prime number")
else :
    print("prime number")
"""

"""
7). Python program to check given number is odd or even.

num9 = int(input("Enter a number: "))
if num9%2==0:
   print("even number")
else :
    print("odd number")
"""

"""
8). Python program to check a given number is part of the Fibonacci series from 1 to 10.

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
num = int(input("Enter a number: "))
if num in fib:
    # Print output
    print("It is a part of the series :", num)
else:
   # Print output
    print("It is not a part of the series :", num)
"""

"""
11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.

num11 = int(input("Enter a number: "))
if num11%2==0 :
    print("square of given number is:", num11**2)
elif num11%3==0 :
    print("square of given number is:", num11**3)
"""

"""
13). Python program to determine whether a given number is available in the list of numbers or not.

list34 = [3, 556, 7, 9, 10, 0]
num12 = int(input("Enter a number: "))
if num12 in list34:
    print(f"{num12} number is available in the list")
else :
    print(f"{num12} number is not available in the list")
    
"""

"""
14). Python program to find the largest number among three numbers.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter another number: "))

if num1>num2 and num1>num3:
    print(f"{num1} is the largest number")
elif num2>num3 and num2>num1:
    print(f"{num2} is the largest number")
elif num3>num1 and num3>num2:
    print(f"{num3} is the largest number")

"""


"""

15). Python program to check any person eligible to vote or not
age > 18+ : eligible
age < 18: not eligible

age = int(input("Enter an age: "))
if age > 18 :
    print(f"{age} is eligible to vote")
else:
    print(f"{age} is not eligible to vote")
"""


"""

num1 = 125
num2 = str(num1)
if num1 == int(num2[::-1]):
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")
    
    
str3 = "jaj"
str4 = str3[::-1]
if str3 == str4:
    print("It is a palindrome number")
else :
    print("It is not a palindrome number")

"""


"""
18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.

marks = int(input("Enter a marks: "))
if marks >= 35:
    print("student passed the exam ")
else :
    print("student failed the exam ")
"""

"""
19). Python program to check whether the given number is positive or not.
Input = 20
Output = True

num13 = int(input("Enter a number: "))
if num13>0:
    print(f"{num13} is a positive number")
else:
    print(f"{num13} is a negative number")
"""

"""
21). Python program to check whether the given number is positive or negative and even or odd.
Input = 26
Output = The given number is positive and even

um5 = int(input("Enter a number: "))
if num5>0:
    if num5%2==0:
        print(f"{num5} is a positive number and even")
    else:
        print(f"{num5} is a positive number and odd")
else :
    if num5 % 2 == 0:
        print(f"{num5} is a negative number and even")
    else:
        print(f"{num5} is a negative number and odd")
"""

"""
22). Python program to print the largest number from two numbers.
Input:
25, 63
Output = 63

n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

if n1>n2:
print(f"{n1} is the largest number")
else:
    print(f"{n2} is the largest number")
"""

"""
23). Python program to check whether a given character is uppercase or not.
Input = A
Output = The given character is an Uppercase

char = input("Enter a character: ")
if char.isupper():
   print(f"{char} is uppercase")
else:
   print(f"{char} is not uppercase")
   
"""

"""
24). Python program to check whether the given character is lowercase or not.
Input = c
Output = True

char1 = input("Enter a character: ")
if char1.islower():
    print(f"{char1} is lowercase")
else:
    print(f"{char1} is not lowercase")

"""

"""
25). Python program to check whether the given number is an integer or not.
Input = 54
Output = True

num1 = int(input("Enter a number: "))
if type(num1)==int:
    print(f"{num1} is a integer")
else:
    print(f"{num1} is not a integer")
    
    

fl = 10.7
if type(fl)==float:
    print(f"{num1} is a float")
else:
    print(f"{num1} is not a float")

str1 = "sqatools"
if type(str1)==str:
    print(f"{str1} is a string")
else:
    print(f"{str1} is not a string")
    

"""

"""
28). Python program to print all the numbers from 10-15 except 13

for num in range(10, 16):
    if num!=13:
        print(num, end=" ")
"""

"""
30). Python program to check whether a given year is a leap or not.
Input = 2000
Output = The given year is a leap year


year= int(input("Enter a year: "))
if(year%100!=0 or year%400==0) and year%4==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
"""

"""
32). Python program to check whether an alphabet is a vowel.

vowel = ["a", "e", "i", "o", "u"]
char = input("Enter a character: ")
if char in vowel:
    print(f"{char} is a vowel")
else:
    print(f"{char} is not a vowel")
"""

"""

33). Python program to check whether an alphabet is a consonant.


char = input("Enter a character: ")
vowel = ["A","E","I","O","U","a","e","i","o","u"]

if char not in vowel:
    print("True")
else:
    print("False")
"""


"""

43). Python program to check whether two numbers are equal or not.
Input:
A=26,B=88
Output = The given numbers are not equal

num1 = 28
num2 = 88

if num1 == num2:
    print("The given numbers are equal")
else:
    print("The given numbers are not equal")
"""