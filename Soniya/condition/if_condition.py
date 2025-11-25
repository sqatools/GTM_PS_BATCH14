a = 50
b = 50

print(a == b)

if a == b:
    print("a and b has equal value :", a, ",", b)
else:
    print("a and b has different value :", a,",", b)

print("_"*50)
# program to check the given number is odd or even
num1 = 12
if num1 % 2 == 0:
    print("This is even number :", num1)
else:
    print("This is odd number :", num1)

#print("This is even :", num1)




print("_"*50)
########## if-elif-else #######

"""
if condi1:
   code1
elif cond2:
   code2
elif cond3:
   code3
else:
   else code
"""

if n == x:
    print("x and n has equal value:", x, n)
elif n == y:
    print("y and n has equal value", y, n)
elif n == z:
    print("z and n has equal value", z, n)
else:
    print("no one has matching value with n")


print("_"*50)
m = 40
if m == x:
    print("x and m has equal value:", x, m)

if m == y:
    print("y and m has equal value", y, m)

if m == z:
    print("z and m has equal value", z, m)
else:
    print("z and m are not equal", z, m)

#######################
p = 40
print("value of P :", p)
p = 50
print("value of P :", p)


print("_"*50)
##############################################
# Nested if condition
round1 =  "pass"
round2 =  "pass"
round3 = "pass"

if round1 == "pass":
    print("congrats 1st round is cleared")
    if round2 == "pass":
        print("congrats 2nd round is cleared")
        if round3 == "pass":
            print("congrats 3rd round is cleared")
        else:
            print("failed in 3rd round, try next time")
    else:
        print("failed in 2nd round, try next time")
else:
    print("failed in 1st round, try next time")
