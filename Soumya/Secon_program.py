def greeting():
    print("Good Morning")
greeting()
greeting()
greeting()

def greeting(a):
    print(a)
greeting(10)
greeting(11)
greeting("test")

#1). Python function program to add two numbers.
"""
print("_"*50)
def addition(n1,n2):
    print(n1+n2)
n1=int(input("Enter a number"))
n2=int(input("Enter another number"))
addition(n1,n2)
"""


#2). Python function program to print the input string 10 times.
"""
print("_"*50)
def string123(str):
    print(str*10)
string=input("Enter a string")
string123(string)
"""

#3). Python function program to print a table of a given number. i*num=a
"""
print("_"*50)
num=int(input("Enter a number"))
def table(num):
    a=0
    for i in range(1, 11):
        a=i*num
        print(i, "*", num, "=", a)
table(num)
"""

#4). Python function program to find the maximum of three numbers.
"""

Input: 17, 21, -9
Output: 21

"""
"""

def maximum(num1,num2,num3):
    if num1>num2 and num1>num3:
        print("maxminum number is:", num1)
    if num2>num3 and num2>num1:
        print("maxminum number is:", num2)
    if num3>num2 and num3>num1:
        print("maxminum number is:", num3)
num1=int(input("Enter a number"))
num2=int(input("Enter another number"))
num3=int(input("Enter another number"))
maximum(num1,num2,num3)

"""

#5). Python function program to find the sum of all the numbers in a list.
"""
Input : [6,9,4,5,3]
Output: 27

"""
print("_"*50)
l = [6,9,4,5,3]
def total(l):
    for val in l:
        t=0
        t += val
    print("Sum of given list: ",t)
total(l)



