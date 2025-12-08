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

"""
   *           # i1 or row 1
*    *         # i2
*    *         #i3
*    *         #i4
  *            #i5


"""

for i in range(1,6): # 5 rows so 1 to 6 because 6 is excluded
    for j in range(1,4): # 3 start per row so 1 to 4
        if i in [2,3,4]:
            if j in [1,3]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i in [1,5]:
            if j in [2]:
                print("*",end=" ")
            else:
                print(" ", end=" ")

    print()