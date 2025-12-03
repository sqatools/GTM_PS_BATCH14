"""
for i in range(6, -1, -1):

    for j in range(i, -1, -1):

        print(" * ", end=" ")
    print()

"""
for i in range(1, 6):
    for j in range(i, 5):
        if i in [1, 5]:
            print(" ")
        else:
            print(" * ", end=" ")

print( )