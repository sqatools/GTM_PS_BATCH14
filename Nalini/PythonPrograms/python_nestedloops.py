"""
for i in range(6, -1, -1):

    for j in range(i, -1, -1):

        print(" * ", end=" ")
    print()

"""
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