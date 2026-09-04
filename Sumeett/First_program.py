a=50
b=50

print (a==b)
if a==b:
    print("a and b are same :", a,b)
else:
    print("a and b are different:", a,b)

A1 = 4
X1 = 1
X2 = 4
X3 = 3
X4 = 4


print("_"*50)

if A1==X1:
    print("A1 and X1 are same")
elif A1==X2:
    print("A1 and X2 are same")
elif A1==X3:
    print("A1 and X3 are same")
else:
    print("A1 and X4 are same")

print("_" * 50)

M1 = 4
if M1 == A1:
    print("M1 and A1 has equal value:", M1, A1)

if M1== X1:
    print("M1 and X1 has equal value", M1, X1)

if M1 == X2:
    print("M1 and X2 has equal value", M1, X2)
if M1 == X3:
    print("M1 and X3 has equal value", M1, X3)
else:
    print("M1 and X4 are not equal", M1, X4)


print ("_"*50)

round1="pass"
round2 = "fail"
#round3 = "pass"

if round1 == "pass":
    print("your first round is cleared", round1)
    if round2 == "fail":
        print("your second round is cleared", round2)
    else:
        print("you are failed in second round", round2)
else:
    print("you are failed in first round", round1)



