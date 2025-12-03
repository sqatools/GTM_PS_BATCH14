#1). Write a Python loops program to find those numbers which are divisible by
# 7 and multiple of 5, between 1500 and 2700 (both included).
#Input1:1500
#Input2:2700

for i in range(1500,2700):
    if i%7==0:
        print(i)

"""2). Python Loops program to construct the following pattern, using a nested for loops.
Output :
*
*  *
*  *  *
*  *  *  *
*  *  *  *  *
*  *  *  *
*  *  * 
*  *
*"""


for i in range(1,6):
    print("* "*i,end=" ")
    print()
for j in range(4,0,-1):
    print("* " *j, end=" ")
    print()

"""3). Python Loops program that will add the word from the user to the empty string using python.
Input: “python”
Output : “python”"""

word=input("Enter the word")
str=""
for i in range(len(word)):
    str +=word[i]

print(str)

"""4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
Output :
Number of even numbers: 4
Number of odd numbers: 5"""
even=0
odd=0
list1=[1,2,3,4,5,6,7,8,9]
for i in list1:
    if i%2==0:
        even +=1
    else:
        odd +=1
print("number of even number:",even)
print("number of odd number:",odd)


"""5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python."""
for i in range(0,7):
    if i==3 or i==6:
        continue
    else:
        print(i)


"""6). Write a program to get the Fibonacci series between 0 to 20 using python.
Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181"""

num1=0
num2=1
count=0
while count<20:
    n2=num1+num2
    print(n2,end=" ")
    num1=num2
    num2=n2
    count +=1
print()

"""7). Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz” 
instead of the number and for multiples of five print “Buzz”.
For numbers that are multiples of both three and five print “FizzBuzz”. """

for i in range(1,31):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", i)
    elif i%3==0:
        print("Fizz",i)
    elif i%5==0:
        print("Buzz",i)









