"""
*
* *
* * *
* * * *
* * * * *




for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=" ")

    print()
"""
print("_"*50)

for i in range(6,0,-1):
    print(i*"*")

print("_"*50)

for j in range(1, 6, 1):
    print(j*"*")

print("_"*50)

"""
- * * * -  # i = 1
* - - - *  # i = 2
* - - - *  # i = 3
* - - - *  # i = 4
* - - - *  # i = 5
- * * * -  # i = 6
"""

for i in range(1, 7):
    for j in range(1, 6):
        if i == 1 or i == 6:
            if j in [1, 5]:
               print(" ", end= " ")
            else:
               print("*", end= " ")
        elif i in[2, 3, 4, 5]:
            if j in [1, 5]:
                print("*", end=" ")
            else:
                print(" ", end=" ")


        else:
          print("*", end = " ")

    print()



