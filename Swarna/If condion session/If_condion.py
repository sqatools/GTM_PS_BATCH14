from importlib.metadata import pass_none

a=50
b=50
print(a==b)
if a==b:
    print("a and b has equal value:",a,",",b)
else:
    print("a and b has different value:",a,",",b)

print("_"*50)

######odd/even######
num1=12
if num1%2==0:
    print(num1,"is even number")
else:
    print(num1,"is odd number")

print("_"*50)

#if-elif-else
n=50
x=40
y=40
z=30

if n==x:
    print("x and n has equal value:",x,n)
elif n==y:
    print("y and n has equal value:",y,n)
elif n==z:
    print("z and n has equal value:",z,n)
else:
    print("no one has matching value with n")


print("_"*50)

m=40
if m==x:
    print("x and m has equal value:",m,x)
if m==y:
    print("y and m has equal value:",m,y)
if m==z:
    print("z and m has equal value:",m,z)

print("_"*50)

#nested if condition

round1="pass"
round2="pass"
round3="pass"

if round1=="pass":
    print("congrats 1st round cleared")
    if round2=="pass":
        print("congrats 2nd round cleared")
        if round3=="pass":
            print("congrats 3rd round cleared")
            print("you are selected")
        else:
            print("sorry you are not selected in 3rd round")
    else:
        print("sorry you are not selected in 2nd round")
else:
    print("sorry you are not selected in 1st round")
