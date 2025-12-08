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

for i in range(10, 1, -1):
    if i == 5:
        break
    print(i)

print("_"*40)

for i in range(10): # i = 0
    if i == 3 or  i == 5 or i == 7:
        continue # police man
    print(i)

    """
    - * * * -  # i = 1
    * - - - *  # i = 2
    * - - - *  # i = 3
    * - - - *  # i = 4
    * - - - *  # i = 5
    - * * * -  # i = 6
    """

    # i is responsible for number of rows
    # j is responsible for number of star in each row
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
            else:
                print(j, end=" ")

        print()

    ####################################

    ################# pattern program ###################
    """
    * - - - -
    * * - - -
    * * * - -
    * * * * -
    * * * * *
    """
    print("-" * 40)

    for i in range(0, 5):
        for j in range(0, i + 1):
            print("*", end=" ")
        print()

    """
    * * * * * 
    * * * *
    * * *
    * * 
    *
    """
    print("-" * 40)

    for i in range(1, 6):
        for j in range(i, 6):
            print("*", end=" ")
        print()

    print("-" * 40)
    """
    * * * * * * 
    * * * * * *
        * *
        * *
        * *
        * *
    """
    for i in range(1, 7):
        for j in range(1, 7):
            if i in [1, 2]:
                print("*", end=" ")
            else:
                if j in [3, 4]:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print()