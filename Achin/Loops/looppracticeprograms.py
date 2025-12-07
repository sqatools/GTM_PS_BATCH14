#1
#pattern program
'''
for i in range(0,5):
    for j in range(0,5):
        if(j<=i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(5,1,-1):
    for j in range(1,i):
        if(j<=i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''
#2
'''
numbers=(1,2,3,4,5,6,7,8,9)
odd=0
even=0
for i in range(len(numbers)):
    if(numbers[i]%2==0):
        even+=1
    else:
        odd+=1

print("The count of odd numbers is",odd)
print("The count of even numbers is",even)
'''

#3
'''
count=1
count1=0
for i in range(1,6):

    for j in range(1,6):
        if(j<=i):
            print(count,end=" ")
            count+=1
            count1=count
        else:
            print(" ",end=" ")
    print()
count1=count-1
#print(count1)

for i in range(5,1,-1):
    for j in range(1,i):
        if(j<=i):
            print(count1-1,end=" ")
            count1-=1
        else:
            print(" ",end=" ")
    print()
'''

'''
#4
for i in range(1,8):
    for j in range(1,8):
        if(i==1 or i==2):
            print("*",end=" ")
        elif(j>2 and j<6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#5
'''
for i in range(1,8):
    for j in range(1,6):
        if(i==1 or i==7):
            if(j==2 or j==3 or j==4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif(i>1 and i<7):
            if(j==1 or j==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
'''
'''
for i in range(1,6):
    if(i==1 or i==5):
        print(" ",end=" ")
    else:
        print("*",end=" ")
print()

for i in range(1,8):
    for j in range(1,6):
        if(i==1 or i==4 or i==5):
            print("*",end=" ")
        elif i in [2, 3, 6, 7]:
            if j == 3:  # middle column empty
                print(" ", end=" ")
            else:
                print("*", end=" ")
    print()  # move to next row
'''

"""
* * * * * * 
* * * * * *
    * *
    * *
    * *
    * *
"""

#6
'''
for i in range(0,6):
    for j in range(0,6):
        if(i==0 or i==1):
            print("*",end=" ")
        elif j in [2,3]:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
'''
#7
'''
for i in range(0,5):
    for j in range(0,5):
        if(i==0 or i==4):
            print("*",end=" ")
        elif j in [0,4]:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''

#8
'''
for i in range(0,5):
    for j in range(0,5):
        if(j==0 and j>=i or j==4 and i not in [1,2,3]):
            print("*",end=" ")
        elif(i==j or i+j==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()
'''

