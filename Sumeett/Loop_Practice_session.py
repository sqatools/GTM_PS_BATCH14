""""
 * * *
*      *
*      *
*      *
*      *
 * * *

"""

for i in range(1, 7):
    for j in range(1, 6):
        if i == 1 or i == 6:
            if j in [1, 5]:
                print("_", end=" ")
        else:
               print("*", end=" ")
    else:
        print("j", end=" ")

    print()