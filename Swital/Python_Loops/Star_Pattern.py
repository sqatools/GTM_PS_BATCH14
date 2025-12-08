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
