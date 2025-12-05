################# pattern program ###################
"""
*
* *
* * *
* * * *
* * * * *
first always check no. of rows and stars count

print("*", end=" ")	prints stars on the same line
print()	moves to the next line
"""
for i in range (1,6):
    # j decide the number of star in each row
    for j in range (1, i+1):
        print("*", end=" ")
    print()


print("_"*10)

############################
"""
print reverse order
* * * * * 
* * * *
* * *
* * 
*
"""
for i in range(5,0, -1):# 5, 4,3,2,1
    # j decide the number of star in each row
    for j in range(1, i+1):#(1, 6),(1,5), (1,4),(1,3),(1,2)
        print("*", end=" ")
    print()

print("_"*10)

############################

"""
  * * *
*       *
*       *
*       *
*       *
  * * *
  """
#here Rows = 6 =i, j= no. of stars in the row
for i in range(1,7):
    for j in range(1,6) :
        if i == 1 or i==6:
            if j in [1,5]:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        elif i in [2,3,4,5]:
            if j==1 or j==5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()

####################################
"""
* * * * * * 
* * * * * *
    * *
    * *
    * *
    * *
"""
#row =6
for i in range(1,7):
    for j in range(1,7):
        if i in [1,2]:
            print("*", end=" ")
        elif i in [2,3,4,5]:
            if j==3 or j==4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()


    
