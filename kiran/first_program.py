a = 10
# a : variable
# = : assignment operator
# 10 : value

print(a, id(a)) # 10 140703904003272

b = 20
c = 30
print("value of a :",a)  # value of a : 10
print("value of b :",b)  # value of a : 20
print("value of c :",c)  # value of a : 30

d = 10
print("value of d :", d, id(d)) # value of d : 10 140703904003272
print("value of d :", d, id(d)) # value of d : 10 140703904003272

x = y = z = 50
print("value of x :", x) # 50
print("value of y :", y) # 50
print("value of z :", z) # 50

#### Assign three different value three variable in one go #####
p, q, r = 80, 90, 100
print("value of p :", p) # 80
print("value of q :", q) # 90
print("value of r :", r) # 100

m = 15
n = 30

v = m + n
print("addition of value :", m+n)
print("addition of value :", v)

e = 35
f = 14

d = e - f
print("substraction of valur :", e-f)
print("substraction of value:", d)

a = 20
b = 20
D = a * b
print("multiplication of value:", a*b)
print("multiplication of value:", d)

a = 2
print("square of value:", a)
