a = 20
# a : variable
# = :  assignment operator
# 20 : value

print(a, id(a)) # 10 140703904003272

a = 30
print(a, id(a)) # 30 140736362096664

a = 10
print(a, id(a)) # 10 140736362096024
print(type(a)) # <class 'int'>

print("_"*30)
a = 50
b = 10
c = 100
f = 6
print("value of a is :", a, id(a)) # value of a is : 50 140736362097304
print("value of b is :", b, id(b)) # value of b is : 10 140736362096024
print("value of c is :", c, id(c)) # value of c is : 100 140736362098904
print("value of c is :", c, id(c)) #value of c is : 100 140736362098904

################### Assign one single value to different variables at a time ####
g = h = i = 40
print(g, h, i) #40 40 40

#### Assign three different value three variable in one go #####
p, q, r = 1, 2, 3
print(p, q, r) # 1 2 3

#####################addition, subtraction, multiplication and division
print(p+q, p-q, p*r) # 3 -1 3
print(a/f) # 8.333333333333334
print(a//f) # 8
print(q%p) # 0

# remainder operator %
v1 = 15
print("v1 divide by 3 remainder :", v1%3) # 0
print("v1 divide by 4 remainder :", v1%4) # 3
print("v1 divide by 7 remainder :", v1%7) # 1

print("_"*50)
# compare values with equal operator (==), not equal operator (!=)
j = 10
k = 20
l = 10
print(j != k) # True
print(j == l) # True
print(j == k) # false


# Repeat string
print(" HI "*5)
#  HI  HI  HI  HI  HI


print("_"*50)
v2 = 600
v3 = 700
print(v2, v3) # 600 700
print(v2, end = " ")
print(v3, end = " ")
print()

print("_"*50)
################### Rules For Variable Name ##########
# 1. Variable name can not contain space in the name
# var 1 =200 # invalid
var_1 = 200  # valid
# var  3 = 10  invalid

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

