'''for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print(i,end=" ")

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

for i in range(6):
    print(i*"*")
    for i in range(4,-1,-1):
        print(i*"*")'''

#   *
#   *  *
#   *  *  *
#   *  *  *  *
#   *  *  *  *  *
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()



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
#*       *
#  * * *

for i in range(1, 6):
    for j in range(1, 8):
            print(" ", end=" ")
    print()
for i in range(1, 7):
    for j in range(1, 8):
        if j == 1 or j == 7:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

