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

for i in range(1, 6):
    if i == 1 or i == 5:
        print("  * * *")
    else:
        print("*", "", "", "", "   *")

























