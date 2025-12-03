"""
Pattern program

for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")

    print()
"""




"""
    
    for i in range(1,6):
    for j in range(1,7-i):
        print("*", end=" ")

    print()

    * * * * *
    * * * *
    * * *
    * *
    *
"""

"""

for i in range(7):
    if i==0 or i==6:
        print("  * * *")
    else :
        print("*" + " " * 7 + "*")
        
for i in range(1, 6):
    if i == 1 or i == 5:
        print("  * * *")
    else:
        print("*", "", "", "", "")
        
 * * *
*       *
*       *
*       *
*       *
*       *
  * * *


"""




"""
for i in range(1, 6):
    for j in range(1, 6):
        print("*", end=" ")
    print()
    
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

"""






"""
for i in range(1, 6):
    if i == 1 or i == 5:
        print("  * * *")
    else:
        print("*", "*", "*", "*", "*")
        
  * * *
* * * * *
* * * * *
* * * * *
  * * *
  
"""
"""
for i in range(1, 6):
    if i == 1 or i == 5:
        print("  * * *")
    else:
        print("*", "", "", "", "   *")
"""

"""
for i in range(1, 7):
    for j in range(1, 6):
        if i==1 or i==2:
           if j in [3, 4]:
               print("_", end="")
           else:
                print("*", end="")
        else i in [2, 3, 4, 5]:
                if i in [1, 5]:
                    print("*", end="")
                else :
                    print(" ", end="")
        else:
            print(j, end="")

"""
"""
for i in range(1, 7):
    for j in range(1, 6):
        if i == 1 or i == 6:
            if j in [1, 5]:
                print(" ", end="")
            else:
                print("*", end="")
        elif i in [2, 3, 4, 5]:
            if j in [1, 5]:
                print("*", end="")
            else:
                print(" ", end="")
        else:
            print(j, end="")
    print()



"""
for i in range(1, 8):
    for j in range(1, 7):
        if i == 1 or i == 2:
            print("*", end=" ")
        elif i in [3, 4, 5,6,7]:
            if j in [3, 4]:
                print("*", end=" ")
            else:
                print(" ", end=" ")

    print()






























