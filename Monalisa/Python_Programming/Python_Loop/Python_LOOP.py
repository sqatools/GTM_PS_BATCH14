"""
->  range output will include the start value and exclude end value in the output
->

"""
#print values from -50 to 9 , step count 3
for i in range(-20, 9, 3):
    print(i,end=" ")

print()

#print values in reverse order
for i in range(10, 2, -1):
    print(i, end=" ")

print()

# No output with range if values are not in range
for i in range(10, 1, 1):
    print(i, end=" ")

print()

# default start value is zero and default step value 1
for j in range(5): # range(0, 5, 1)
    print(j,end=" ")
print()

list1 = [2,4,6,8,10,12]
"""
for val in list1:
    print(val)
for i in range(0,len(list1),2):
    print(list1[i],end=" ")"""

for i in range(len(list1)-1,-1,-2):
    print(list1[i],end=" ")

print()

'''while loop'''
m=1
while m<=10:
    print(m)
    m+=1
'''from 1 to 10, check number is odd /even'''
p=1
while p<=10:
    if p%2==0:
        print(p,"is even")
    else:
        print(p,"is odd")
    p+=1

print("*",50)
'''CONTINUE statement'''
s=11
count =0
for i in range(2,s):
    if s%2==0:
        count=count+1
        break
    else:
        continue

if count>0:
    print(s,"is not prime")
else:
    print(s,"is prime")


'''pattern'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

for i1 in range(5,0,-1):
    for j1 in range(i1,0,-1):
        print("*",end=" ")
    print()