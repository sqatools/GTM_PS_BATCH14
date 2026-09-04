#1). Python Program to addition two integer values.

a=int(input("Enter the value of a :"))
b=int(input("Enter the value of ab :"))
sum=a+b
sub=a-b
mul=a*b
avg=sum/2
print("The sum of a & b :",sum)

#2). Python Program to subtract two integer values.
print("The sub of a - b :",sub)

#3). Python program to multiply two numbers.
print("The multiplication of a * b :",mul)

#4). Python program to repeat a given string 5 times.
"""
Input :
str1 = “SQATools”
Output :
“SQAToolsSQAToolsSQAToolsSQAToolsSQATools”
"""
str1='SQATools'

print("printing the SQATools 5 times:",str1*5)
print(str1)

print("-----"*20)
#5). Python program to get the Average of given numbers.
#Formula: sum of all the number/ total number

print("average of given number:",avg)

"""6). Python program to get the median of given numbers.
Note: all the numbers should be arranged in ascending order
Formula : (n+1)/2
n = Number of values
Input : [45, 60, 61, 66, 70, 77, 80]
Output:  66
"""
print("-----"*20)
list1=[10,20,30,40,50,60]
#shorting the list1 in assending order

list1.sort()
n=len(list1)

if n %2 == 1:  #5%2=>1
    median=list1[n//2] #5//2
    print(median)
else:
    median=(list1[n // 2 - 1] + list1[n // 2]) / 2
    print("Need to write code for it")
    print(median)
print("-----"*20)

#7). Python program to print the square and cube of a given number.
a=int(input("Enter a number to find the square and cobe of it:"))
print("Square of a number is:",a**2)
print("Cube of a number is:",a**3)

print("-----"*20)

#8). Python program to interchange values between variables.

a = 10
b = 20
print("The value of a before swapping:",a)
print("The value of b before swapping:",b)
#defining a number where we are adding the sum of two i/p numnbers
c = a+b      #30
a = c-a      #10
b = c-b      #10

print("The value of a after swapping:",a)
print("The value of b after swapping:",b)

print("-----"*20)

#9). Python program to solve this Pythagorous theorem.
#Theorem : (a2 + b2 = c2)
a=10
b=20
c=a**2+b**2
Pythagorous_theorem=c**2
print("Pythagorous_theorem")
