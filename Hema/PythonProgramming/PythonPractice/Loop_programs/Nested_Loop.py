"""2). Python Loops program to construct the following pattern, using a nested for loops.
Output :
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*"""
# Increasing part of the pattern
for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()
# Decreasing part of the pattern
for i in range(4, -1, -1):
    for j in range(i):
        print("*", end=" ")
    print()
"""
this is not nested:
for j in range(1,6):# or just write in range(6)
    print(j*" *")
for k in range(4,-1, -1):
        print(k*" *")
"""

# print values from 1 to 10 using while loop
num = 1
while num <=10:
    print(num)
    num += 1

print("_"*20)

#get all odd numbers from 1 to 20
num1 = 1
while num1 <=20:
    if num1 % 2!=0:
        print(num1)
    num1 += 1

print("_"*20)
