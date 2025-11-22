#program 1 - WAP to add 2 integers
a=10
b=23
print("sum of a& b=", a+b, type(a+b))

#program 2 - WAP to subtract 2 integers
a=10
b=23
print("diff of a& b=", a-b, type(a-b))

#program 3 - WAP to multiply  2 integers
a=10
b=23
print("prod of a& b=", a*b, type(a*b))

#Python program to repeat a given string 5 times.
str1 = "SQATools"
print(str1*5)

#Python program to get the Average of given numbers
a=20
b=30
c=40
print("average=", (a+b+c)/3)

#Python program to get the median of given numbers.

#Python program to print the square and cube of a given number.
print("square=", a**2)
print("cube=", a**3)

#Python program to interchange values between variables.
a,b=b,a
print("value of a after interchange is ", a)
print("value of b after interchange is", b)

#Python program to solve this Pythagorous theorem.
a=6
b=8
c=10
lhs= (a**2)+(b**2)
rhs= c**2
print("a^2+b^2",lhs)
print("c^2",rhs)
print(lhs==rhs)

#Python program to solve this square theorem (a+b)^2
lhs= (a+b)**2
rhs= a**2+b**2+2*a*b
print("(a+b)^2= a^2+b^2+2ab",lhs,lhs==rhs)

#Python program to solve this square theorem (a-b)^2
lhs= (a-b)**2
rhs= a**2+b**2-2*a*b
print("(a+b)^2= a^2+b^2-2ab",lhs,lhs==rhs)

#Python program to solve this square theorem a**2-b**2
lhs= a**2-b**2
rhs= (a+b)*(a-b)
print("a**2-b**2",lhs,lhs==rhs)

#Python program to solve this cube  theorem (a + b)3 = a3 + 3ab(a+b) + b3
lhs= (a + b)**3
rhs= a**3 + 3*a*b*(a+b) + b**3
print("(a + b)^3",lhs,lhs==rhs)

#Python program to solve this cube  theorem (a – b)3 = a3 – 3a2b + 3ab2 – b3
lhs= (a - b)**3
rhs= a**3 - 3*a*b*(a-b) - b**3
print("(a - b)^3",lhs,lhs==rhs)

#Python program to calculate the area of the square.
print("Area of square",a*a)
