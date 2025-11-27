# if condition
a=10
b=20
if a==b:
    print("equal:",a,"=".b)
else:
    print("not equal:",a,"!=",b)

############### even odd number check

num=12
if num%2==0:
    print("even")
else:
    print("odd")

###############3if elif
n=10
x=20
y=0
z=10
if n==x:
    print("n==x")
elif n==y:
    print("n==y")
elif n==z:
    print("n==z")
else:
    print("not equal")
 ##################################################

 #if nested

r1="pass"
r2="fail"
r3="pass"
if r1=="pass":
    print("r1 is cleared")
    if r2=="pass":
        print("r2 is cleared")
        if r3=="pass":
            print("r3 is cleard")
        else:
            print("r3 is failed")
    else:
        print("r2 is failed")

else :
    print("r1 is failed")

