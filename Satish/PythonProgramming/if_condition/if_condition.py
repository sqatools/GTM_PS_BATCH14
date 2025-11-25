a=20
b=30
if a==b:
    print("a and b are equal",a,b)
else:
    print("a and b are not equal",a,b)

####if elif to check multiple conditions
num= 15
x=10
y=20
z=30
# In this if any one condition true then it will comeout from block.
if num==x:
    print("num and x are equal")
elif num==y:
    print("num and y are equal")
elif num==z:
    print("num and z are equal")
else:
    print("num is not matching with anyone")

# Nested if else

percentage=61

if percentage>33:
    print("pass")
    if (percentage>50 and percentage<60):
        print("Second division")
        if percentage>60:
            print("first division")
        else:
            print("Second division")
    else:
        print("Third Division")


else:
    print("fail")



