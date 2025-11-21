a = 10
# a : variable
# = :  assignment operator
# 10 : value

print(a, id(a)) # 10 140703904003272

b = 20
c = 30
print("value of a :",a )  # value of a : 10
print("value of b :",b )  # value of b : 20
print("value of c :",c )  # value of c : 30

d = 10
print("value of d :", d, id(d)) # value of d : 10 140703904003272
print("value of d :", d, id(d)) # value of d : 10 140703904003272

################### Assign one single value to different variables at a time ####
x = y = z = 50
print("value of x :", x) # 50
print("value of y :", y) # 50
print("value of z :", z) # 50


#### Assign three different value three variable in one go #####
p, q, r = 70, 80, 90
print("value of p :", p) # 70
print("value of q :", q) # 80
print("value of r :", r) # 90


print("_"*50)
##### Math operation with data ###
m = 12
n = 20
# Add with plus operator +
v = m + n
print("addition  of value :", m+n)  # addition  of value : 32
print("addition of value :", v)  # addition  of value : 32

print("multiplication :", m*n) # 240
print("division with single /:", n/3)  # 6.666666666666667
print("division with double //:", n//3) # 6
print("subtraction :", m-n)

# power operator **
print("square of any value :", m**2)  # square of any value : 144
print("cube of n :", n**3)  # cube of n : 8000

# remainder operator %
v1 = 15
print("v1 divide by 3 remainder :", v1%3)
print("v1 divide by 4 remainder :", v1%4)
print("v1 divide by 7 remainder :", v1%7)

print("_"*50)
# compare values with equal operator (==), not equal operator (!=)
j = 10
k = 20
l = 10
print(j != k) # True
print(j == l) # True

# Repeat string
print(" Hello "*5)
#  Hello  Hello  Hello  Hello  Hello


print("_"*50)
v2 = 600
v3 = 700
print(v2, v3) # 600 700
print(v2, end=" ")
print(v3, end=" ")
# 600 700

print()
print("_"*50)
################### Rules For Variable Name ##########
# 1. Variable name can not contain space in the name
# var 1 =200 # invalid
var_1 = 200  # valid

# 2. There is no length limit for variable name
a = 30 # valid
hello_we_Are_learning_python = 50 # valid

# 3. Variable name can not start with number.
# 1var = 60 # invalid
var_123_value = 500 # valid


# 4. Variable name can not contain special except underscore.
# name&user = 'Mohan' # invalid
user_name = "Mohan" # valid


# 5. Variable names are case-sensitive.
name = "Rahul"
Name = "Rohit"
NAME = "Raman"
NAme = "Raghav"
print(name , "|", Name, "|", NAME, "|", NAme)
# Rahul | Rohit | Raman | Raghav


username = "Mohan"
age = 29
city = "Mumbai"
# My name is Mohan and age is 29 and living in mumbai
print("My name is ", username," and age is ", age, " and living in ", city)

print("_"*50)
#############################################
# (a+b)^2 = a^2 + b^2 + 2ab
a = 10
b = 20
lhs = (a+b)**2
rhs = a**2 + b**2 + 2*a*b
print(lhs)
print(rhs)
print(lhs == rhs)  # True















