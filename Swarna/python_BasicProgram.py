#Add two integers
num1=30
num2=40
sum=num1+num2
print("sum of num1 and num2 is:",sum)

################ different way#

num1=30
num2=40
print("Addition of num1+num2 is:",num1+num2)

#Subtraction of two integers
num3=50
num4=20
sub=num3-num4
print("Subtraction of num3 and num4 is:",sub)

#multiplication of two integers
num1=20
num2=40
print("Multiplication of num1 and num2 is:",num1*num2)

#Program to repeat a given string five times.
str1="Python "
n1=5
print("Repetition of str1 five times is:",str1*n1)

#program to get the average of given numbers.

a=30
b=20
c=40
print("average of three numbers is:",(a+b+c)/3)

'''#program to get the median of given no.s.
#example list of values
values=[10,20,30,40,50]
#sort the list
values.sort()
#get length of the list
n=len(values)

if n % 2 == 1:
    median_value = values[n // 2]
else:
    median_value = (values[n // 2 - 1] + values[n // 2]) / 2

print(f"The median is: {median_value}")'''

#print square and cube of given no.
n=9
print("Square of n is:",n**2)
print("Cube of n is:",n**3)

#program to interchange between variables.
a=50
b=70
a,b=b,a
print("value of a:=",a)
print("value of b:=",b)

#Solve given math formula
# (a+b)^2=a^2+b^2+2ab

a=2
b=3
result=a**2+2*a*b+b**2
print("(a+b)^2 is:",result)

# (a-b)^2=a^2+b^2-2ab

a=2
b=3
result=a**2-2*a*b+b**2
print("(a-b)^2 is:",result)

#a^2-b^2=(a-b)(a+b)
a=3
b=2
result=(a+b)*(a-b)
print("a^2-b^2 is:",result)

#solve (a+b)^3=a^3+b^3+3ab(a+b)

a=3
b=2
result=a**3+3*a*b*(a+b)+b**3
print("(a+b)^3 is:",result)

#solve  (a – b)3 = a3 – 3a2b + 3ab2 – b3
'''
a=3
b=2
result=a**3-3*a*b*(a-b)-b**3
print("(a-b)^3 is:",result)'''

# area of the square
side=int(input("enter the side of the square:"))
print("area of the square:", side**2)

# calculate area of circle

radius=int(input("Enter radius of circle:"))
pi=3.14
area=pi*radius**2
print("Area of circle is:",area)

"""# calculate simple interest
P=int(input("Enter principal amount:"))
R=float(input("Enter rate of interest:"))
T=int(input("Enter time in years:"))
SI=(P*R*T)/100
print("Simple Interest is:",SI)"""

#print current date
import datetime
date=datetime.datetime.now()
print(date.strftime ("%y %b %d") )