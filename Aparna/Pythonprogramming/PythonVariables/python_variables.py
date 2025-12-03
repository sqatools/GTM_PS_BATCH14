a = 10
# a=variable
# = : assignment operator
# 10 = value
print(a, id(a))
# 10 1512461435408

b = 20
c = 30
print("value of a:", a)
print("value of b:", b)
print("value of c:", c)

d = 10
print("value of d:", d, id(d))

### Assign one single value of diff variables at one time
x = y = z = 50
print("value of x:", x)
print("value of y:", y)
print("value of z:", z)

### Assign 3 different value there variables at one go
p, q, r = 70, 80, 90
print("value of p:", p)
print("value of q:", q)
print("value of r:", r)

### math operators
m = 12
n = 20
v = m + n
print("addition of value:", m + n)
print("addition of value:", v)
print("multiplication: ", m * n)
print("division with single/:", n / 3)
print("division with double//:", n // 3)

## Add with plus operator
print("subtraction:", m - n)

## power operator **
print("square of any value:", m ** 2)
print("cue of n:", n ** 3)

##  Remainder operator %
V1 = 15
print("v1 divide by 3 remainder:", v % 3)
print("v1 divide by 4 remainder:", v % 4)
print("v1 divide by 7 remainder:", v % 7)

print("_" * 50)

## Compare  values with == and !=
j = 10
k = 20
l = 10
print(j != k)
print(j == l)

## Repeat string
print(" Hello " * 3)

v2 = 600
v3 = 700
print(v2)
print(v3)
print(v2, end="")
print(v3, end="")
print(v2, v3)

## Rules for variable name
## 1.variable cannot contain space for name
var_1 = 200
# var 1 =  100 invalid

## 2. There is no length limit for var
a = 30
hello_we_are_learning = 50

## 3. variable cannot start with number
## 1var = 60
var_123 = 500

## 4.variable name cannot contains special character except underscore
# name & user = 'mohan'
user_name = 'mohan'

## 5. variable names are case senstive
name = 'Rahul'
NaMe = 'Neha'
NAME = 'vinod'
print(name , "|", NaMe, "|", NAME)

