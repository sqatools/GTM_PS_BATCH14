a = 10
b = 20
if a == b:
    print("a and b has equal value:, a,b")
else:
    print("Both are different values, a,b")

    ############### even or odd ##################
    a = 14
    if a%2 == 0:
        print("It is a odd number, a")
    else:
        print(" It is an even number,a")
#####################if_elif_else condition###############

x = 10
y = 20
z = 40
v = 20

if x == y:
    print("x and y has equal value", x,y)
elif y == z:
    print("y and z are equal values", y,z)
elif y == v:
    print("y and v have equal value",y,v)
else:
    print("All values are different")

    x = 10
    y = 20
    z = 40
    v = 20

    if x == y:
        print("x and y has equal value", x, y)
    elif y == z:
        print("y and z are equal values", y, z)
    elif y == x:
        print("y and v have equal value", y, x)
    else:
        print("Only y and z have equal values")

     ########################################################

    p = 50
    print("Value of p:", p)
    ####################Nested condition###########################

### write a python program to check weather the given number is divisible by 2 and 4 ################
num1 = input ("Please enter the value:")
print(num1, type(num1))
x = int(num1)

if x%2 == 0 and x%4 == 0:
    print("This number is divisible by 2 and 4:", x)
else:
    print("This number is divisible by 2 and 4:", x)

    ####### write a program to accept students marks to provide their marks and results###########
marks = int(input("Please enter your marks:"))

if marks <= 30:
    print("Failed in Exam")
elif marks > 30 and marks <= 60:
print(" 3rd Division")
elif marks > 60 and marks <= 80:
print(" 2nd Division")
elif marks > 80 and marks <= 100:
print(" 1st Division")
else:
print("Marks should not be greater than 100")












