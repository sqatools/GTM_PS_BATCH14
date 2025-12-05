# Start with simple for loop syntax
# for i in range(start_value, end_value, step[increase and decrease])
# print 1 to 15
import math

print("#" * 50)
for i in range(1, 15, 1):
    print(i)

# print 1 to 15 with step value 2 means increase by 2 alternate value
print("#" * 50)
for i in range(-50, 10, -2):
    print(i)

# print -50 to 10
for i in range(-50, 10, 1):
    print(i)
# other way
print("#" * 50)
for i in range(10, -50, -1):
    print(i)

# print -50 to 10 with step value 2 means increase by 2 alternate value
print("#" * 50)
for i in range(-50, 10, 2):
    print(i, end="")
# print only even numbers from 1 to 50
print("#" * 50)
for i in range(2, 50, 2):
    print(i, end="")

############################# String ################################################
print("#" * 50)
str2 = "AutomationTest"
for val in str2:
    print(val)

############################# List ################################################

print("#" * 50)
list1 = [3, 5, 1, 5, 1, 5, 6, 7, 8]
for val in list1:
    print(val)

############################# tuple ################################################

print("#" * 50)
tup1 = (3, "hi", 50 + 3j, [1, 2, 3])
for val in tup1:
    print(val)

# WAP to get even number from list using if condition
print("#" * 50)
list2 = [3, 4, 2, 5, 6, 2, 5, 7, 8, 12]
for val in list2:
    if val % 2 == 0:
        print(val)

############################Nested Loop#####################################
print("#" * 50)
for i in range(4):
    print(" i range value: ", i)
    for j in range(3):
        print(" j range value: ", j)

    print("#" * 30)

############################ While Loop ####################################
print("#" * 50)
n = 1
while n <= 5:
    print(n)
    n += 1

############################ Continue Statement ####################################
print("#" * 50)
n = 1
while n <= 10:
    if n == 2:
        n += 1
        continue
    print(n)
    n += 1

############################ Break Statement ####################################
print("#" * 50)
n1 = 1
while n1 <= 10:
    if n1 == 3:
        break
    print(n1)
    n1 += 1

############################ Infinite loop ####################################
print("#" * 50)
n1 = 1
while n1 >= 1:
    print(n1)
    n1 += 1
    if n1 == 1000:
        break

print("#" * 50)
while True:
    print(n1)
    n1 += 1
    if n1 == 2000:
        break

################## Prime number check ########################################
print("#" * 50)
pnum = int(input("Enter the number: "))
count = 0
for i in range(2, pnum):
    if pnum % i == 0:
        count += 1
        break
    else:
        continue
if count > 0:
    print(pnum, "is a not prime number")
else:
    print(pnum, "is a prime number")

#######################################Other way###############################################
print("#" * 50)
pnum = int(input("Enter the number: "))

if pnum <= 1:
    print(pnum, "is not a prime number")
else:
    is_prime = True
    for i in range(2, pnum):
        if pnum % i == 0:
            is_prime = False
            break

    if is_prime:
        print(pnum, "is a prime number")
    else:
        print(pnum, "is not a prime number")

#######################################Other way###############################################
print("#" * 50)
pnum = int(input("Enter the number: "))

if pnum <= 1:
    print(pnum, "is not a prime number")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(pnum)) + 1):
        if pnum % i == 0:
            is_prime = False
            break

    if is_prime:
        print(pnum, "is a prime number")
    else:
        print(pnum, "is not a prime number")

#######################################Pattern ########################################
print("#" * 50)
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")

    print()
#######################################Pattern ########################################
"""
* * * * * 
* * * *
* * *
* * 
*
"""
print("#" * 50)
for i in range(1, 6):
    for j in range(1, 7 - i):
        print("*", end=" ")

    print()

print()
print("#" * 50)
for i in range(6, 1, -1):
    for j in range(i, 1, -1):
        print("*", end=" ")

    print()

print("#" * 50)
for i in range(5, 0, -1):
    print("* " * i)
print("#" * 50)
for i in range(1, 6):
    print("* " * (6 - i))
print("#" * 50)
for i in range(5):
    print("* " * (5 - i))

#######################################Pattern ########################################
"""
  * * *
*       *
*       *
*       *
*       *
*       *
  * * *
"""
print("#" * 50)
for i in range(1, 7):
    for j in range(1, 6):
        if i in [1, 6]:
            if j in [1, 5]:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        elif i in [2, 3, 4, 5]:
            if j in [1, 5]:
                print("*", end=" ")
            else:
                print(" ", end=" ")

    print()

####################Print T pattern #####################
print("#" * 50)
for i in range(1, 7):
    for j in range(1, 7):
        if i in [1, 2]:
            print("*", end=" ")
        elif i in [3, 4, 5, 6]:
            if j in [3, 4]:
                print("*", end=" ")
            else:
                print(" ", end=" ")

    print()
