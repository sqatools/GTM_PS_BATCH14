# range(start, end value, step)
"""
->  range output will include the start value and exclude end value in the output
->

"""
# print values from 1 to 10
for i in range(1, 11, 1):
    print(i)


print("_"*40)
# print values from 1 to 10 with step value 2
for i in range(1, 10, 2):
    print(i)


print("_"*40)
# print value in reverse order from 5 to 1
for i in range(5, 0, -1):
    print(i)

"""
5
4
3
2
1
"""

print("_"*40)
# print value in reverse order till -5
for i in range(2, -6, -1):
    print(i)

"""
2
1
0
-1
-2
-3
-4
-5

"""


print("_"*40)
# No output with range if values are not in range
for i in range(10, 1, 1):
    print(i)


print("_"*40)
# default start value is zero and default step value 1
for j in range(5): # range(0, 5, 1)
    print(j)


print("_"*40)
# Apply loop of different data types:
list1 = [5, 7, 8, 2, 5, 18]

for val in list1:
    print(val)

print("_"*40)
# Apply loop on tuple
tup1 = ('a', 'b', 'c', 234)
for val in tup1:
    print(val)


print("_"*40)
# Apply loop on string
str1 = "Programming"
for char in str1:
    print(char)

print("_"*40)
# write loop with if condition and get all even number from given list

list2 = [5, 7, 9, 2, 13, 14]
for val in list2:
    if val%2 == 0:
        print(val, end=" ")

###################################
print()
print("_"*40)
for i in range(6, 14, 2):
    print(i)


print("_"*40)
#########################################################
# Nested loop condition.

# Address: outer loop
for i in range(1, 6, 1): # i = 1, 2, 3, 4, 5
    print("Address : i=",i)
    # package : inner loop
    for j in range(1, 4, 1): # j = 1, 2, 3
        print("Package : j=", j)

    print("_"*20)


print("_"*40)
#########################################################


# While loop condition.
"""
while cond:code
"""

# print values from 1 to 10 using while loop
num = 1
while num <= 5:
    print(num)
    num += 1
    #num = num + 1

print("_"*50)
# get all the odd number from 1 to 20
n1 = 1
while n1 <= 20:
    # check the odd value
    if n1%2 != 0:
        print(n1)
    # increase n1 value by 1
    n1 += 1

print("_"*40)
########################### continue and break statement #############
# continue statement: when the continue condition is satisfied then it will move loop to next interation
# without executing the remaining code.

# print values from 1 to 10 with continue statement
v1 = 1
while v1 <= 10: # v1 = 1, 2, 3, 4
    if v1 == 3 or v1 == 7 or v1 == 5:
        v1 += 1
        continue

    print(v1) # 1, 2, 4
    v1 += 1 # 2, 3, 5



print("_"*50)
# break statement: once the code is satisfied with break condition then loop will terminate immediately.


m = 1
while m <= 10:
    if m == 5:
        break
    print(m)
    m += 1


print("_"*50)
# infinite loop
g = 1
# default condition value is True
while True:
    print(g)
    # increase the value by 1
    g += 1
    # compare g value with 10000
    if g == 10000:
        break

print("_"*50)
#################################################
# write a python program to check given number is prime or not

# take input from user
num = 17
count = 0
for i in range(2, num):
    print("i:",i)
    # check the number is divisible by i
    if num%i == 0:
        # increase counter if value is divisible by any value
        count += 1
        break
    else:
        continue

# outside of the loop check the counter value still same or changed.
if count > 0:
    print("This is not prime number :", num)
else:
    print("This is prime number :", num)


print("_"*50)
################# pattern program ###################
"""
*
* *
* * * 
* * * *
* * * * *
"""

# i decide the row number
for i in range(1, 6): # i =1, 2, 3, 4, 5
    # j decide the number of star in each row
    for j in range(1, i+1): # (1, 2)(1, 3)(1, 4)(1, 5)(1, 6)
        print("*", end=" ")

    print()

"""
* 
* * 
* * * 
* * * * 
* * * * * 
"""
# Home work
#1
"""
* * * * * 
* * * *
* * *
* * 
*
"""

# 2
"""
  * * *
*       *
*       *
*       *
*       *
*       *
  * * *
"""

print("_"*40)
# Explanation prime number program
num = 12 # user input
prime = True # consider this number prime
for i in range(2, num): #(2, 17)
    print("i:",i) # 2
    # check the number is divisible by i
    if num%i == 0: # (12%2 == 0)
        # increase counter if value is divisible by any value
        prime = False
        break



if prime is True:
    print("This is prime number :", num)
else:
    print("This is not a prime number :", num)





