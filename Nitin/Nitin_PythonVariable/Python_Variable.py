a=10
# a ->variable
# =  ->Operator
# 10 ->Value
print(a, id(a)) #10  140728195052064
print(a)

b=20
c=30

################### Assign one single value to different variables at a time ####
x = y = z = 50
print("Value of x:",x)
print("Value of y:",y)
print("Value of z:",z)

#### Assign three different value three variable in one go #####
a,b,c=20,30,40
print("The value of a:",a)
print("The value of b:",b)
print("The value of c:",c)

print("_"*50)
##### Math operation with data ###
a=10
b=20

sum=a+b
multi=a*b
print("The sum of a & b: ",sum)
print("The multi of a*b:",multi)
print("The division of a/b: ",a/b) #float
print("The division of a//3: ",10//3)
print("The modulus of b%3: ",20%3)

# power operator **
print("Square of 2:",2**2)
print("Square of 2:",2**3)

print("_"*50)
# compare values with equal operator (==), not equal operator (!=)
a=10
b=20
c=10
print(a==c) #True
print(a!=c) #False


"print("_"*50)"