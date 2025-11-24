# 1) addition of 2 numbers
num1 = 20
num2 = 30
total = num1 + num2
print("Total num1 and num2 :", total)
num3, num4 = 50, 60
print("Total num1,num2,num3 and num4 is:", total+num3+num4)
print("data type of total:", type(total))
print("*" * 50)

a = 345345.94856
b = 98445.498359
print("Total a nd b is:", a+b)
print("data type of a:", type(a))

# 2) subtraction of numbers
x = 60
y = 70
print("difference:", x-y)
p = 30.56
q = 23.54
print("difference of p and q:", p - q)
print("*" * 20)

# 3) multiply two numbers

"""
m = 45634
n = 85464
product = m * n
print("product of m and n: ", product)
print("data type of product variable:", type(product))
print("data type of  variable: m is", type(m))
print("*", * 20)
"""
m = 456.857486
n = 854648686868768.9847596
product = m * n
print("product of m and n: ", product)
print("data type of product variable:", type(product))
print("data type of  variable: m is", type(m))
print("*" * 50)

# 5) Python program to repeat a given string 5 times

string = "Grotech "
print(string *5)
print(string *4)
print(string *3)
print(string *2)
print(string *1)

print("*" * 50)
# 6. Python program to get the Average of given numbers.
a = 10
b = 30
c = 40
average = (a + b + c) / 3
average1 = (a + b + c) // 3
print("Average is : ", average)
print("Average round off: : ", average1)
print("*" * 50)


# 7. Python program to print the square and cube of a given number.

x = 6
y = 9
square = x ** 2
cube = y ** 3
print("square is : ", square)
print("cube  is : ", cube)
print("*" * 50)

# 8 interchange the values between variables.
x = 20
y = 30
x, y = y, x
print("x and y", x, y)
print("*" * 50)

# 9 program to solve the given math formula.Pythagorous theorem.
# Theorem : (a2 + b2 = c2)
import math

a = 4
b = 2

c = math.sqrt(a**2 + b**2)

print("Hypotenuse (c) =", c)
print("*" * 50)

# 10). Python program to solve the given math formula.
# (a + b)^2 = a^2 + b^2 + 2ab

a = 5
b = 4
lhs = (a + b) ** 2
print (lhs)
rhs = (a ** 2) + (b ** 2) + (2 * a * b)
print(rhs)
print("*" * 50)

# 11. python program to solve the given math formula.
# Formula : a^2 – b^2 = (a-b)(a+b)

a = 4
b = 6
lhs = (a ** 2) - (b ** 2)
print (lhs)
rhs = (a - b) * (a + b)
print(rhs)
print("*" * 50)
# 12 Python program to calculate simple interest.


princAmount = 3000
rate = 12
time = 2
interest = (princAmount * rate * time) / 100

print("Interest amount:", interest)

print("*" * 50)

# Python program to reverse a given number.
a = 123
x = a // 10
print(x)

# 13. program on  a string

name = "Tanvi"

print(name[0])

