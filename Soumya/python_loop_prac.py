"""
1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
Input1:1500
Input2:2700


for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print(i, end=" ")

"""

"""
2). Python Loops program to construct the following pattern, using a nested for loops.
Output :
*
*  *
*  *  *
*  *  *  *
*  *  *  *  *
*  *  *  *
*  *  * 
*  *
*


for i in range(1,6):
    for j in range(1,i+1): #(1,2)(1,3)(1,4)(1,5)(1,6)
        print("*", end=" ")
    print()
for i in range(5, 1, -1):
    for j in range(i, 1, -1):
        print("*", end=" ")
    print()
    
"""

"""
3). Python Loops program that will add the word from the user to the empty string using python.
Input: “python”
Output : “python”

word = input("Enter a word: ")
str1 = " "
for i in range(len(word)):
    str1 += word[i]
print(str1)

#Enter a word: test
#test

"""

"""
4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
Output :
Number of even numbers: 4
Number of odd numbers: 5

Input = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for i in Input:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)

"""

"""
5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
0 1 2 4 5 

for i in range(0, 7):
    if i!=3 and i!=6:
        print(i, end=" ")
"""

"""
6). Write a program to get the Fibonacci series between 0 to 20 using python.
Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181

num1 =0
num2 =1
count = 0
while count < 20:
    print(num1, end=" ")
    n1=num1+num2
    num1=num2
    num2=n1
    count+=1
"""



    
