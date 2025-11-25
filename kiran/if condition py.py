a = 40
b = 40

print(a == b)

if a == b:
    print("a and b has equal valur:", a,b)

else:
    print("a and b has differnt value:", a,b)


print("_"*50)
# program to check the number is odd or even

num1 = 15
if num1% 2 == 0:
    print("This is even number:", num1)

else:
    print("This is odd number:", num1)

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
n = 50
x = 40
y = 40
z = 30

if n == x:
    print("x and n has equal value:", x, n)
elif n == y:
    print("y and n has equal value", y, n)
elif n == z:
    print("z and n has equal value", z, n)
else:
    print("no one has matching value with n")
