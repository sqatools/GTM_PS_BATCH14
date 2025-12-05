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
    
"""



"""
s3 = "Virat Is Best Batsman of India"
#output 1 = VViratt iiss BBestt BBatsmann ooff IIndiaa
#output 2 = airat ss Best Batsman of IndiV
#output 3 = tiraV sI tseB namstaB fo aidnI

"""
s3 = "Virat Is Best Batsman of India"
output1 = (s3[0]+s3[0:5]+s3[4]+" "+s3[6]+s3[6:8]+s3[7]+" "+s3[9]+s3[9:13]+s3[12]+" "+s3[14]+s3[14:21]+s3[20]+" "+s3[22]+s3[22:24]+s3[23]+" "+s3[25]+s3[25:30]+s3[29])
print(output1)
print("*"*40)
output2 = (s3[0].replace("V", "a")+s3[1:5]+" "+s3[6:8]+" "+s3[9:13]+" "+s3[14:21]+" "+s3[22:24]+"  "+s3[25:29]+s3[-1].replace("a","V"))
print(output2)

print("*"*4)
output3 = (s3[-26]+s3[1:4]+s3[0]+" "+s3[7]+s3[6]+" "+s3[12]+s3[10:12]+s3[9]+" "+s3[20]+s3[15:20]+s3[14]+" "+s3[23]+s3[22]+" "+s3[-1]+s3[-4:-1]+s3[-5])
print(output3)














































































