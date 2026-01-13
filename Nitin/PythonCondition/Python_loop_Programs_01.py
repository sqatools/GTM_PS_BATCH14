"""
1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
Input1:1500
Input2:2700
"""
count=0

for i in range(1500 ,2701):
    if i%7==0 and i%5==0:   # i should be divisible by 7 and 5
        print(i,end=",")
        count=count+1
print(count)

"""
3). Python Loops program that will add the word from the user to the empty string using python.
Input: “python”
Output : “python”
"""
str1='python'
str2=''
for i in str1:
    str2=str2+i
    #print(str2)
print("str2=",str2)

print("======="*10)
"""
4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
Output :
Number of even numbers: 4
Number of odd numbers: 5
"""
even_count=0
odd_count=0
for i in range(1 ,10):
    if i%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print('odd_count:',odd_count)
print('even_count:',even_count)

print("======="*10)
"""
5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
"""
for i in range(7):
    if i==3 or i==6:
        continue
    else:
        print(i, end=",")
print()
print("======="*10)
"""
6). Write a program to get the Fibonacci series between 0 to 20 using python.
Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
"""
print("======="*10)
num1=0
num2=1
for i in range(5):
    print(i)
    print(num1 , end=" ")
    n=num1+num2
    num1=num2
    num2=n
print("--")
print("======="*10)

print("---Fibonacci Series-------")
num1=0
num2=1
i=0
while i<5:
    print(num1,end=' ')
    n=num1+num2
    num1=num2
    num2=n
    i=i+1

print("")
print("======="*10)
"""
7). Write a program that iterates the integers from 1 to 30 using python. 
For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
For numbers that are multiples of both three and five print “FizzBuzz”. 
"""

for i in range(31):
    if  i%3==0 and   i%5==0:
        print("FizzBuzz")
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif  i%3==0 and   i%5==0:
        print("FizzBuzz")
    else:
        pass