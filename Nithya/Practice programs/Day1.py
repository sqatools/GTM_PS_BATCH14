#1). Python Program to add two integer values.
Salary =100
Incentive = 20
print("1. Takehome:", Salary+Incentive)

#2). Python Program to subtract two integer values.
Salary = 100
Expenses= 150
print("2. Inhand:", Salary-Expenses)

#3). Python program to multiply two numbers.
Salary=150
New_offer= Salary*2

print("3. New Package:",Salary*New_offer) #(150*150*2 = 45000)

#4). Python program to repeat a given string 5 times.
Val="Just Kidding"
print("4. Result",Val*5)

#5). Python program to get the Average of given numbers.
a = 40
b = 50
c = 30
print("5.Sum of all number /Total number:", (a+b+c)/3) # response with "/" will have a decimal
print("Sum of all number //Total number:", (a+b+c)//3) # response with "//" will have value before decimal


#Python program to get the median of given numbers.
#Note: all the numbers should be arranged in ascending order
''' 
Formula : (n+1)/2
n = Number of values
Input : [45, 60, 61, 66, 70, 77, 80]
'''

a,b,c,d=12,24,30,40

print("6. Formula:(n+1)/2", a/5) ## list s not taught yet

# Python program to print the square and cube of a given number.

num1=9
print("7. Sqaure of num1:", num1**2)
print("Cube of num1:", num1**3)

#Python program to interchange values between variables.
a = 10
b = 20
a,b=b,a
print ("8. value of b in a :", a)
print ("value of a in b :", b)

#9). Python program to solve this Pythagorous theorem.
#Theorem : (a2 + b2 = c2)
a=2
b=3
c= a**2 + b**2
print ("Result:", c**2)

# 10). Python program to solve the given math formula.
# Formula : (a + b)2 = a^2 + b^2 + 2ab
a=b=4
print("10.Result:", a**2+b**2+2*a*b)

# 11). Python program to solve the given math formula.
# Formula : (a – b)2 = a^2 + b^2 – 2ab
a,b=2,4
C= (a**2+b**2-2*a*b)
print("11.Result for (a-b)^2):", C)

#12). Python program to solve the given math formula.
#Formula : a2 – b2 = (a-b)(a+b)
LHS= a**2 - b**2
RHS= (a-b) * (a+b)
print("12.Result for a2 – b2 =(a-b)(a+b):",LHS==RHS)
# 13.Python program to solve the given math formula.
#Formula : (a + b)3 = a3 + 3ab(a+b) + b3
Left=(a+b)**3
Right =(a**3)+3*a*b*(a+b)+b**3
print("13. Result:",Left==Right)
#14.Python program to solve the given math formula.
#Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3
Index1= 3*a**2*b
Index2=3*a*b**2
Left= (a-b)**3
Cube= a**3-Index1+Index2-b**3
print("14. result :a-b^3", Cube)
print("14. result :a-b^3", Left==Cube)

#15). Python program to calculate the area of the square.
Formula : area = a*a

print("15. Area:", a*a )

'''
16.Python program to calculate the area of a circle.
Formula = PI*r*r
r = radius
PI = 3.14'''
r=2
PI=3.14
print ("16. Area of Circle:PI*r^2", PI*r*r)
# 17). Python program to calculate the area of a cube.
# Formula = 6*a*a
a=268762308759
print("17. Area of Cube:", a**3)

'''18.+Python program to calculate the area of the cylinder.
Formula = 2*PI*r*h + 2*PI*r*r'''
r=8
h=12
Area= 2*PI*r*h + 2*PI*r*r
print("18.Area of Cylinder:", Area)

'''19). Python program to check whether the given number is an Armstrong number or not.
Example: 153 = 1*1*1 + 5*5*5 + 3*3*3'''
Amstrong_or_Not=172
a=1
b=7
c=2
Right= a**3+b**3+c**3
print("19. Finding Amstrong#:",Amstrong_or_Not==Right)

'''20). Python program to calculate simple interest.
Formula = P+(P/r)*t
P = Principle Amount
r = Anual interest rate
t = time'''
P = 1000
r = 9.8
t = 3
Total_Interest= P+(P/r)*t
print("20.Simple Interest:", Total_Interest)

print("#"*50)
'''22). Python program to calculate days between 2 dates.
Input date : (2023, 1, 5) (2023, 1, 22)
Output: 17 days'''
Start, End = (2023-1-5),(2023-1-22)
print("22. No. of days between two dates:" , int(Start-End))

'''23). Python program to get the factorial of the given number.'''

A=23
print("23. Factorial is:", A%2)








