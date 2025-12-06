print("X"*20,"02-12-2025","X"*20 )
print("\t \t \t \t While Loop")

# print values from 1 to 10 using while loop
i=0
while i <= 10:
    print(i)
    i=i+1
    print("X"*20)

# get all the even number from 1 to 20

for i in range(1,21):
    if i%2==0:
        print(i)
    else:
        continue
print("X"*30)
# skip values 5,10 from 1 to 10 with continue statement
a=1
while a <= 10:
    if a%5==0:
       a+=1
       continue
    else:
        print(a)
        a += 1

print("X"*30)
# break statement practice
for Count in range (1,10):
    print(Count)
    if Count==5:
        print("Match found", Count)
        break
else:
    print("No match found",Count)

print("X"*30)
#print Angular pattern upside Triangle
print("Printing Angular Pattern")
for i in range(6, 1, -1): # 6
    for j in range (i, 1, -1): #(6, 1, -1)
        print("*", end=" ")

    print()

print("X"*30)
#print Angular pattern T

print("Printing T Pattern")
'''
1 2 3 4 5 6 
1 2 3 4 5 6 
    3 4 
    3 4 
    3 4 
    3 4 
'''
for i in range (1,7):
    for j in range(1,7):
        if i in [1, 2]:
            print("*", end=" ")
        elif i in [3,4,5,6]:
            if j in [1,2, 5, 6]:
                print(" ", end=" ")
            else:
                print("*", end=" ")


    print()

print("X"*30)
#printing 0
"""
  345   # i=1
1234567 # i=2
1234567 # i=3
1234567 # i=4
  345   # i=5
"""
for i in range(1,6):
    for j in range(1,8):
        if i in [1,5]:
            if j in [3,4,5]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [2,3,4]:
            if j==1 or j==7:
               print("*", end=" ")
            else :
                print (" ",end=" ")

    print()

    print("*"*10)






