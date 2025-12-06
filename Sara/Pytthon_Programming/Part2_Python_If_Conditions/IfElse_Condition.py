#************** Demo ****************

print("-"*15,"Demo","-"*15)

a=10
b=40

print("a:",a)
print("b:",b)
if a==b:
    print("a and b are equal :", a,",",b)
else:
    print("a and b are not equal :", a, ",", b)

#************** Program 1 ****************

print("-"*15,"Program 1 : Check if No. is +ve or -ve","-"*15)

num1=int(input("Enter a number :"))
print("Entered number is ", num1)

if num1 > 0:
    print(num1,"is positive")
else:
    print(num1, "is negative")

print("")
#************** Program 2 ****************3
print("-"*15,"Program 2 : Check if No. is Even or Odd","-"*15)

num2=int(input("Enter a Number without decimal :"))
print("Entered number is ", num2)

if num2%2==0:
    print(num2,"is an Even number")
else:
    print(num2, "is an odd number")

print("")
#************** Program 3 ****************3
print("-"*15,"Program 3 : Check if No. is divisible by 5 ","-"*15)

num3=int(input("Enter a Number without decimal :"))
print("Entered number is ", num3)

if num3%5==0:
    print(num3,"is divisible by 5")
else:
    print(num3, "is not divisible by 5")

print("")

#************** Program 4 ****************3
print("-"*15,"Program 4 : Check if a number is divisible by both 3 and 5 ","-"*15)

num4=int(input("Enter a number :"))
print("Entered number is :",num4)

if num4%3==0 and num4%5==0:
    print(num4, "is divisible by both 3 and 5")
else:
    print(num4, "is not divisible by both 3 and 5")

print("")

#************** Program 5 ****************3
print("-"*15,"Program 5 : Find the largest of two numbers ","-"*15)

num5=int(input("Enter Number 1: "))
num6=int(input("Enter Number 2: "))

print("Entered Numbers are: ",num5,num6)

if num5>num6:
    print(num5,"is greater than", num6)
else:
    print(num6,"is greater than", num5)

