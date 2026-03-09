#1. To add/substract/multiply two integer values

a=10
b=20
c=a+b
s=a-b
m=a*b
print("addition of two values:",c)
print("substraction of two values:",s)
print("multiplication of two values:",m)

print("_"*50)

#2. print given string into five times

str="SQATools"
print("five times string:",str*5)

print("_"*50)

#3. avg of given number

a=40
b=50
c=30
avg=(a+b+c)/3
print("average of number:",avg)

print("_"*50)

#4. Python program to print the square and cube of a given number.

num1=9
square=num1**2
cube=num1**3
print("square of the value:",square)
print("cube of the value:",cube)

print("_"*50)

#5. Python program to interchange values between variables.

a = 10
b = 20
#a,b=b,a
a=b
b=10
c=b
print("value of a:",a)
print("value of c:",c)

print("_"*50)

#6. Python program to solve the given math formula.
#Formula : (a + b)2 = a^2 + b^2 + 2ab
#Formula : (a – b)2 = a^2 + b^2 – 2ab
#Formula : a2 – b2 = (a-b)(a+b)

a = 10
b = 20
result1=a**2+b**2+2*a*b
result2=a**2+b**2-2*a*b
result3=a**2-b**2
result4=(a-b)*(a+b)
R=(result3==result4)
print("(a + b)2 :",result1)
print("(a - b)2 :",result2)
print("val of res3:",result3)
print("val of res4:",result4)
print("res3=res4:",R)

print("_"*50)

#(a + b)3 = a3 + 3ab(a+b) + b3
#(a – b)3 = a3 – 3a2b + 3ab2 – b3

R1=a**3+3*a*b*(a+b)+b**3
print("(a + b)3:",R1)

print("_"*50)

R2=a**3-3*a**2*b+3*a*b**2-b**3
print("(a - b)3:",R2)

print("_"*50)

#Python program to calculate the area of the square.
#Formula : area = a*a

a=6
area=a*a
print("area:",area)

print("_"*50)

#Python program to calculate the area of a circle.
#Formula = PI*r*r
#r = radius
PI = 3.14
r=4
circle=PI*r*r
cube=6*a*a
#input("Enter radius of circle: ")
print("area of circld:",circle)
print("area of the cube:",cube)

print("_"*50)

#pythagorous theorem
a=3
b=4
c=5
lhs=a**2+b**2
rhs=c**2
r3=(lhs==rhs)
print("value of a2+b2:",lhs)
print("value of c2:",rhs)
print("value of r3:",r3)

print("_"*50)

# median
















