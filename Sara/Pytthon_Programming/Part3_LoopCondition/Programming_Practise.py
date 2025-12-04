'''

* * * * * *
* * * * * *
    * *
    * *
    * *
    * *
'''

for i in range (1, 7):
        for j in range (1,7):
            if i in [3,4,5,6]:
                if j in [1,2,5,6]:
                    print(" ", end=" ")
                else:
                    print("*", end=" ")
            else:
                print("*", end=" ")
        print(" ")