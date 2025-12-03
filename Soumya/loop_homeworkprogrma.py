"""
for i in range(1, 6): # i =1, 2, 3, 4, 5
    # j decide the number of star in each row
    for j in range(1, i+1): # (1, 2)(1, 3)(1, 4)(1, 5)(1, 6)
        print("*", end=" ")

    print()
"""

for i in range(1, 6):
    for j in range(1, i+5):
        print("*", end=" ")

    print()
