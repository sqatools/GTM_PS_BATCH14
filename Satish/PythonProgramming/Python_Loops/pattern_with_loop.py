"""
* * * * * * # i=1
* * * * * * # i=2
    * *     # i=3
    * *     # i=4
    * *     # i=5
    * *     # i=6
"""
for i in range(1,7):
    for j in range(1,7):
        if i in [1,2]:
            print("*",end=" ")
        elif i in [3, 4, 5, 6]:
            if j in [3, 4]:
                print("*", end=" ")
            else:
                print(" ", end=" ")

    print()
