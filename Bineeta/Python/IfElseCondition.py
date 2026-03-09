a = 100
b = 100
print(a == b)

if a == b:
    print("a and b has equal value :", a, b)
else:
    print("a and b has different value :", a,",", b)

print("_"*50)
#to check the given number is odd or even
num1 = 45
if num1 % 2 == 0:
    print("This is even number :", num1)
else:
    print("This is odd number :", num1)
#print("This is even :", num1)

print("_"*50)
## if-elif-else ##
n = 50
a = 40
b = 40
c = 30

if n == a:
    print("a and n has equal value:", a, n)
elif n == b:
    print("b and n has equal value", b, n)
elif n == c:
    print("c and n has equal value", c, n)
else:
    print("no one has matching value with n")

print("_"*50)
m = 40
if m == a:
    print("a and m has equal value:", a, m)

if m == b:
    print("b and m has equal value", b, m)

if m == c:
    print("c and m has equal value", c, m)
else:
    print("c and m are not equal", c, m)

########################################################################################################
a1 = 20
print("value of A1 :", a1)
p = 40
print("value of A1 :", a1)


print("_"*50)
#####################################################################################################
# Nested if condition
round1 =  "pass"
round2 =  "pass"
round3 = "pass"

if round1 == "pass":
    print("congrats 1st round is cleared")
    if round2 == "pass":
        print("2nd round is cleared")
        if round3 == "pass":
            print("3rd round is cleared")
        else:
            print("failed 3rd round, try next time")
    else:
        print("failed 2nd round, try next time")
else:
    print("failed 1st round, try next time")
