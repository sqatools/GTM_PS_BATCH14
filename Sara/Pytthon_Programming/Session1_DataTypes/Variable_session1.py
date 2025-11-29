# hash is used for single line comment. python is dynamic programming language
# if you try to concatenate integer and string it will throw error as iys not allowed; print(a+8)-- will throw error
# a- variable; 10= value; = assignment operator
a = 10
print(a, id(a))  # 10 140725249746328

print("-" * 50)
# space before and after equal is optional. ur print will still work if you give b=20 but you will get format alert
b = 20
print("b value", b)  # b value 20

print("-" * 50)
# ************# assigning SAME VALUE TO different variables.

a = b = c = 30
print(a, b, c)  # 30 30 30
print("value of a", a)  # value of a 30
print("value of b", b)  # value of b 30
print("value of c", c)  # value of c 30

print("-" * 50)
# **************************** Assigning 3 different values to 3 different cariables at one's.

e, f, g = 10, 20, 30
print(e, f, g)
print("value of e", e)  # value of e 10
print("value of f", f)  # value of f 20
print("value of g", g)  # value of g 30

print("-" * 70)
# working with operators
m = 40
n = 30
p = m + n
print(p)  # 70
print("addtion :", p)  # addtion : 70
print("subtraction", m - n)  # substraction 10
print("multiplication :", m * n)  # multiplication : 1200
print("division with single / :", m / n)  # division with single / : 1.3333333333333333
print("division with double // :", m // n)  # division with double // : 1

print("-" * 100)
# ******************POWER OPERATOR (**)
a = 4
b = 8
print("SQUARE OF", a ** 2)  # SQUARE OF 16
print("cube of 4", a ** 3)  # cube of 4 64

print("-" * 100)
# ********** REMINDER OPERATOR %
s1 = 30
print("s1 divide by 3 reminder :", s1 % 3)  # s1 divide by 3 reminder : 0
print("s1 divide by 4 reminder :", s1 % 4)  # s1 divide by 4 reminder : 2

print("-"*100)
# ********* COMPARISION OPERATOR WILL RETURN TRUE/FALSE : EQUAL TO(==) and NOT EQUAL TO (!=)
e = 2
f = 4
g = 2

print("E=2 and F=4 are equal:", e==f) #E=2 and F=4 are equal: False
print("E=2 and F=4 are not equal:", e!=f) #E=2 and F=4 are not equal: True
print("E=2 and g=2 are equal:", e==g) #E=2 and g=2 are equal: True
print("E=2 and g=2 are equal:", e!=g) #E=2 and g=2 are equal: False

print("-"*100)
# REPEAT STRING
print("Demo "*3)

print("-"*100)

#adding multiple print value in single line
s=10
d=20

print(s) #these 2 print statement will print value in 2 separate line
print(d)
print(s, end=" ") #This will print both value in 1 single line 10 20
print(d)

print("-"*100)

#*******RULES FOR WRITING VARIABLE*****

# 1. Variable name can not contain space in the name
# var 1 =10 # invalid
var_1 = 10  # valid

# 2. There is no length limit for variable name
a = 10 # valid
pythonvariable_session1 = 5 # valid
#3. Variable name can not start with number.
# 1v = 12 # invalid
var_123_check = 30 # valid

# 4. Variable name can not contain special except underscore.
# var%name = 'Sara' # invalid
var_name= "Sara" # valid


# 5. Variable names are case-sensitive.
name = "Sara"
Name = "Aish"
NAME = "Dev"
NAme = "Sim"
print(name , "|", Name, "|", NAME, "|", NAme)
#Sara | Aish | Dev | Sim

username = "Sim"
age = 24
city = "Mumbai"
# My name is Mohan and age is 29 and living in mumbai
print("My name is ", username," and age is ", age, " and living in ", city)
