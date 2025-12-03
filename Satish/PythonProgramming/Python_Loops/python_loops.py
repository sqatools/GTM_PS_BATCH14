
for val in range(1,10,1):
    print(val)

print("_"*50)
list1=[1,2,3,4,5]
for val in list1:
    print(val)

print("_"*50)
tupl1=(4,5,6,7,8)
for val in tupl1:
    print(val)

# Nested for loop
print("_"*50)
for address in range(1,6):
    print("address",address)
    for packet in range(1,4):
        print("packet",packet)

# While loop
# Note: we use for loop if we know no of iteration and if we don't know no of iteration then we use while loop.We also use while loop for infinte loop.
print("_"*50)
i=0
while i<=10:
    print(i)
    i+=1

# break: we use break key word to come out from loop but not from program.
# continue: we use continue keyword to skip any value
print("_"*50)
for i in range(1,5):
    if i==3:
        break
    print(i)

print("_"*50)
for i in range(1,5):
    if i==3:
       continue
    print(i)

"""
*  row1
** row2
*** row3
**** row4
***** row6

assume "*" as col
"""

print("_"*50)

for row in range(1,7):
    for col in range(1,row+1):
        print("*",end=" ") # use end=" " to avoid \n bydefault by print statement
    print() # this print statement is used to add newline

'''
Explanation: Outer loop runs for each row
Inner loop print "*"
end=" " keeps star in one row
print() moves to next row
'''


"""
******  row1
*****    row2
****     row3
***    row4
**   row5
*  row6

consider "*" as a col
"""
print("_"*50)
for row in range(6,0,-1):
    for col in range(row):
        print("*",end=" ") # use end=" " to avoid \n bydefault by print statement
    print() # this print statement is used to add newline

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
print("_"*50)
for row in range(1,8):
    for col in range(1,2):
        if row==1 or row==7:
            print(" ",end="")
            print("*"*3,end="")
            print(" ", end="")
            print()
        else:
            print("*", end="")
            print(" "*3,end="")
            print("*", end="")
            print()


        # else:
        #     print("*",end="")
        #     print(" "*3)
        #     print("*", end="")
        #     print()

# for i in range(5):
#     print("i",i)
#     for j in range(2):
#         print("j",j)