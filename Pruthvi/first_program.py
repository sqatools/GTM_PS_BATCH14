print("hello world")
a = 100
b = 50
# a : variable
# = : assignment operator
# 100 : value
print(a,id(a))
print(b,id(b))
b = 40
c = 30
print("value of a :",a )
print("value of b :",b )
print("value of c :",c )
d=90
print("value of d :",d,id(d)) ##value of d:90 140726719983512

##### assign a single value at a time for multiple variables
a=b=c=10
print("value of a :",a) #10
print("value of b :",b) #10
print("value of c :",c) #10

#### assign five different values for different variables at a time
c,d,e,f,g =10,20,30,40,50
print("value of c :",c) #10
print("value of d :",d) #20
print("value of e :",e) #30
print("value of f :",f) #40
print("value of f :",g) #50

print("%"*10)

#### match operator with data
a = 10
b = 20
# add with plus operator +
c = a+b
print("value of addition :",a+b) #30
print("total addition value :",c) #30

# add with multiplication operator *
a = 10
b = 20
print("value of multiplication :",a*b) #200

# add with division with single /
a = 10
b = 20
print("value of division :",b/3) #6.666666666666667

# add with division with double //
a = 10
b = 20
print("value of division :",b//3) #6

# add with minus with operator -
a = 10
b = 20
print("value of subtraction :",b-a) #10

# power operator **
a = 10
b = 20
print("square of any value :",a**2) #100
print("square of any value :",a**3) #1000
print("square of any value :",b**4) #160000

# reminder operator %
t = 30
print("t devide by 4 reminder :",t%4) #2
print("t devide by 6 reminder :",t%6) #0
print("t devide by 2 reminder :",t%2) #0

# compare with equal operator(==) and not equal operator (!=)
j = 10
k = 20
l = 10
print(j!=k) #true
print(j==l) #true

# repeat string
print("hello "*6)

print("_"*20)
v1 = 200
v2 = 300
print(v1,v2)

a = 10
b = 20
print(a,b)

print(v1, end=" ")
print(v2, end=" ")

## rules for valiable name
# 1.variable name can not contain space in the name
# var 1 = 100 # invalid
var_1 = 100 # valid

# 2.there is no length limit for variable value
a= 20 # valid
hi_we_are_learning_python = 50 # valid

# 3.variable name can not start with number
# 1var = 20 # invalid
var_132_value = 40 # valid

# 4.variable name can not contain special symbols except underscore
# user&name = 'raj' # invalid
user_name  = 'raj' # valid

# 5.variable names are case sensitive
name = "Rahul"
Name = "ROHit"
NAME = "Raman"
NAme = "Raghav"
print(name , "$", Name, "|", NAME, "|", NAme)

## my name is pruthvi age is 35 and living in chittoor
user_name = "pruthvi"
age = 35
city ="chittoor"
print("my name is",user_name,"age is",age,"living in",city)

# (a+b)^2 = a^2 + b^2 + 2ab
a = 10
b = 20
lhs = (a+b)**2
rhs = a**2 + b**2 + 2*a*b
print(lhs)
print(rhs)
print(lhs == rhs)  # True






