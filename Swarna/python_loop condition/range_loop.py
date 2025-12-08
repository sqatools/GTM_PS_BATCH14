#print values fron 1 to 10 using range loop
for i in range(1, 11):
    print(i)

#print value from 1 to 10 with step 2
for i in range(1, 10, 2):
    print(i)

#print value in reverse order from 10 to 1
for i in range(10, 0, -1):
    print(i)

print("_"*40)
#print value in reverse order till -5
for i in range(2, -6, -1):
    print(i)

print("_"*40)
# no output with range if values are not in range.
for i in range(10,1,1):
    print(i)

# default start value is 0 and default step is 1
print("_"*40)
for j in range(5):  # range(0, 5, 1)
    print(j)

print("_"*40)
# apply loop of different data types
list1=[5,7,8,2,5,18]
for val in list1:
    print(val)

print("_"*40)
#   Apply loop on tuple
tup1=('a','b','c',234)
for val in tup1:
    print(val)

print("_"*40)
#   Apply loop on string
str1="Hello"
for char in str1:
    print(char)

print("_"*40)
# Write loop with if condition and get all even numbers from given list.
list2=[5,7,9,2,13,14]
for val in list2:
    if val%2==0:
        print(val,end=" ")

print()
print("_"*40)
for i in range(6,14,2):
    print(i)

print("_"*40)
##########################################
# nested loop condition
#Address:outer loop
for i in range(1,6,1):
    print("Address:i=",i)
    for j in range(1,4,1):
        print("Package:j=",j)

    print("_"*20)
print("_"*40)

###########################################
######### WHILE LOOP ##################
# while loop condition
'''while cond:
    code
    '''
# print values from 1 to 10 using while loop
num=1
while num<=10:
    print(num)
    num+=1
    #num=num+1

print("_"*50)
# Get all the odd numbers from 1 to 20 using while loop
n1=1
while n1<=20:

    if n1%2!=0:
        print(n1)
    n1+=1

print("_"*50)

################ Continue and `Break statement ################
# Print values from 1 to 10 with continue statement

v1=1
while v1<=10:
    if v1==3 or v1==7 or v1==5:
        v1+=1
        continue
    print(v1)
    v1+=1

print("_"*50)

# Break statement: once the code is satisfied with break condition then loop will terminate immediately.

m=1
while m<=10:
    if m==6:
        break
    print(m)
    m+=1

print("_"*50)

# Infinite loop:
g=1
#default condition is true
while True:
    print(g)
    g+=1
    if g==10000:
        break

#############################################
# WAP IN PYTHON to check given number is prime or not
# take input from user
num=9
count=0
for i in range(2,num):
    print("i:",i)
    if num%i==0:
        count+=1
        break
    else:
        continue

if count>0:
    print("This is not a prime number:",num)
else:
    print("This is a prime number:",num)



#############################################

#   *
#   *  *
#   *  *  *
#   *  *  *  *
#   *  *  *  *  *
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

print("_"*40)

# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print("*", end=" ")
    print()

#  * * *
#*       *
#*       *
#*       *
#*       *
#  * * *








for i in range(1,7):
    for j in range(1,7):
        if i in[1,2]:
            print("*",end=" ")
        elif i in[3,4,5,6]:
            if j in [3,4]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        else:

            print(" ",end=" ")

    print()



for i in range(1, 10):
    if i == 5 or i == 7:
        continue
    print(i)

print("_"*40)
for i in range(1, 10):
    if i == 5:
        break
    print(i)


