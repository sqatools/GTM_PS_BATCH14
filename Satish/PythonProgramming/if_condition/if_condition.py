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

round1="pass"
round2="pass"
round3="pass"

if round1=="pass":
    print("Eligible for 2 round")
    if round2=="pass":
        print("Eligible for 3rd round")
        if round3=="pass":
            print("Selected")
        else:
            print("failed in 3 round")

    else:
        print("Failed in 2 round")


else:
    print("Try next time")



