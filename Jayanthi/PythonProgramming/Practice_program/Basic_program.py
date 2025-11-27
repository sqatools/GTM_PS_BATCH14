# 1). Python Program to add two integer values.
Number1=10
Number2=20
print("Value of num1+num2 is ",Number1+Number2)

# 2). Python Program to subtract two integer values.

print("Value of num1-num2 is ",Number1-Number2)

# 3). Python program to multiply two numbers.

print("Value of num1*num2 is ",Number1*Number2)

"""4). Python program to repeat a given string 5 times.
 Input :
# str1 = “SQATools”
# Output :
# “SQAToolsSQAToolsSQAToolsSQAToolsSQATools” """
print("SQATools"*5)

"""5). Python program to get the Average of given numbers.
Formula: sum of all the number/ total number
Input:
a = 40
b = 50
c = 30
Output :
Average = 40"""

a = 40
b = 50
c = 30
Average=(a+b+c) // 3
print("Average=",Average)

""" 7). Python program to print the square and cube of a given number.
Input :
num1 = 9
Output :
Square = 81
Cube =   729 """

num1=9
print("Value of num1 square",num1,"is", num1**2)
print("Value of num1 cube", num1, "is", num1**3)

"""8). Python program to interchange values between variables.
Input :
a = 10
b = 20
Output :
a = 20
b = 10"""
a = 10
b = 20
a,b=b,a
print (a)
print(b)

"""9). Python program to solve this Pythagorous theorem.
Theorem : (a2 + b2 = c2)"""
import math
x = 3
y = 4

res = math.hypot(x, y)
print(res)

"""
10). Python program to solve the given math formula.
Formula : (a + b)2 = a^2 + b^2 + 2ab
"""
p=8
q=6
lhs=(p+q)**2
rhs= (p**2)+(q**2)+(2*p*q)

print(lhs)
print(rhs)

"""11). Python program to solve the given math formula.
Formula : (a – b)2 = a^2 + b^2 – 2ab"""
lhs=(p-q)**2
rhs= (p**2)+(q**2)-(2*p*q)
print(lhs)
print(rhs)

"""12). Python program to solve the given math formula.
Formula : a2 – b2 = (a-b)(a+b)"""
lhs=(p**2)-(q**2)
rhs=(p-q)*(p+q)
print(lhs)
print(rhs)

"""13). Python program to solve the given math formula.
Formula : (a + b)3 = a3 + 3ab(a+b) + b3 """
print("cube")
lhs=(p+q)**3
rhs=(p**3)+(q**3)+(3*p*q*(p+q))
print(lhs)
print(rhs)

"""14). Python program to solve the given math formula.
Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3"""
p=8
q=6
lhs=(p-q)**3
print(lhs)
rhs=(p**3)-(3*(p**2)*q)+(3*p*(q**2))-(q**3)
print(rhs)

"""15). Python program to calculate the area of the square.
Formula : area = a*a"""
a=10
area=a*a
print(area)

"""16). Python program to calculate the area of a circle.
Formula = PI*r*r
r = radius
PI = 3.14"""
r=3
PI = 3.14
print((r**2)*PI)

"""17). Python program to calculate the area of a cube.
Formula = 6*a*a"""
a=4
Formula = 6*a*a
print(Formula)

"""18). Python program to calculate the area of the cylinder.
Formula = 2*PI*r*h + 2*PI*r*r"""
r=3
h=4
PI = 3.14
Formula = 2*PI*r*h + 2*PI*r*r
print(Formula)

"""20). Python program to calculate simple interest.
Formula = P+(P/r)*t
P = Principle Amount
r = Anual interest rate
t = time"""
P=4000.50
r=10
t=5
Formula = P+(P/r)*t
print(Formula)

"""21). Python program to print the current date in the given format
Output: 2023 Jan 05
Note: Use the DateTime library"""
import datetime
date = datetime.datetime.now()

print(date.strftime (" %Y %b %d "))


"""22). Python program to calculate days between 2 dates.
Input date : (2023, 1, 5) (2023, 1, 22)
Output: 17 days"""
from datetime import date
date_1 = date(2023, 1, 5)
date_2 = date(2023, 1, 22)
print(date_1)
print(date_2)
result = (date_2 - date_1).days
print("difference between days ",result)




















