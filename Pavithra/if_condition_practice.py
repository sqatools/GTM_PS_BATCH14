a = 50
b = 452

if a==b:
     print("Both a and b are equal")
else:
    print("a and b is not equal")

print("*"*50)

a = 35
if a%2:
    print("a is even")
else:
    print("a is odd")

print("*" * 50)


p = 52
n = 50
u = 30
o = 588
if n==p:
    print("n is same like p")
elif u==p:
    print("u is  same like p")
elif o==p:
    print("o is same like p")
else:
    print("Nothing is same")

print("*"*50)

round1 = "fail"
round2 = "pass"
round3 = "pass"

if round1=="pass":
    print("You cleared round1")
    if round2=="pass":
        print("You cleared round2 ")
        if round3=="pass":
            print("You cleared round3")
        else:
            print("you didn't clear round3")
    else:
            print("you didn't clear round2")
else:
        print("you didn't clear round1")
