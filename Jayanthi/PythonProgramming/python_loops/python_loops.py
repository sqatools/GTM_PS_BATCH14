# range(start,end,step)
for i in range(10,20,1):
    print(i)

print("_"*50)

for i in range(5): # when the start and step is not given
    print(i)

print("-"*50)

for i in range(5,-5,-1):
    print(i)

str1='programming'
for i in str1:
    print(i)
print('_'*50)
list1=[3,5,6,7,8,9]
for i in list1:
    print(i)

print('_'*50)
for i in range(10,15,2):
    print("Address of i",i)
    for j in range(5,-8,-1):
        print('door bell',j)

# all the odd num between 1 to 20

print('_'*50)
num=1
while num<=20:
    if num%2!=0:
        print(num)
    num +=1


# Continue and Break stmt
print("-"*50)
v1=1
while v1<=10:
    if v1==3 or v1==5 or v1==7:
        v1 +=1
        continue
    print(v1)
    v1 +=1

print("-"*50)
m1=1
while m1<=10:
    if m1==3 or m1==5 or m1==7:
        m1 +=1
        break
    print(m1)
    m1 +=1

"""# infinite loop
print("-"*50)
g=1
while True:
    print(g)
    g +=1"""

#Print the Prime number
print("-"*50)
num=7
count=0
for i in range(2,num):
    print(i)
    if num%i==0:
        count +=1
        break
    else:
        continue

if count >0:
    print(num," not a prime number")
else:
    print(num,"This was prime number")

# pattern
"""
*
**
***
****
*****
"""
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")

    print()

"""
*****
****
***
**
*
"""
print("-"*50)
for i in range(6,1,-1):
    for j in range(i-1):
        print("*",end=" ")

    print()


"""
 ***
*   *
*   *
*   *
 ***
"""
print("-"*50)
for i in range(1,6):
    if i==1 or i==5:
        print(" ",end="")
    else:
        print("*",end="")
print()

for j in range(1,6):
    if j==1 or j==5:
        print("*", end="")
    else:
        print(" ", end="")
print()

for k in range(1,6):
    if k==1 or k==5:
        print("*", end="")
    else:
        print(" ", end="")
print()

for l in range(1,6):
    if l==1 or l==5:
        print(" ",end="")
    else:
        print("*",end="")
print()

print("-"*50)
for i in range(1,6):
    if i==1 or i==5:
        for j in range(1,6):
            if j ==1 or j==5:
                print(" ",end="")
                continue
            else:
                print("*",end="")
        print()

    else:
        for k in range(1,6):
            if k==1 or k==5:
                
                print("*",end="")
            else:
                print(" ",end="")
        print()















