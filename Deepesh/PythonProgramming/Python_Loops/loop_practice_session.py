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
"""
* * * * * * 
* * * * * *
    * *
    * *
    * *
    * *
"""


