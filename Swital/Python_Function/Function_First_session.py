# Function without parameter
def program():
    print("Hi")


# Function with parameter
def program_value(s):
    print(s)


# call by value:
print("call by value:")
program_value("Hello, user")

# call by reference
print("call by reference: ")
a = "Data for Python"
program_value(a)


# Function with 2 parameter
def summation(a, b):
    print(f"Summation of {a} and {b} is: ", a + b)


summation(10, 20)


# Interchange the variable in print
def summation1(a, b):
    print(f"Summation of {a} and {b} is: ", b + a)


summation1(10, 20)


# 2 variables but one has default value
def multiplication(a, b=9):
    print("Multiplication of this: ", a * b)


multiplication(6)


# two variables but one has default value and call both values by other values
def multiplication(a, b=9):
    print("Multiplication of this: ", a * b)


multiplication(6, 10)


# three variables but one has default value
def multiplication1(a, b, c=7):
    print("Multiplication of this: ", a * b * c)


multiplication1(6, 10)


# three variables but two has default value and update c value in call time
def multiplication2(a, b=9, c=7):
    print("Multiplication of this: ", a * b * c)


multiplication2(a=6, c=10)


# three variables but two has default value and update all values

def multiplication3(a, b=9, c=7):
    print(f"Multiplication of {a}, {b}, and {c} are: ", a * b * c)


a = b = c = 10
multiplication3(a, b, c)


# Four variables and update all with reference variable
def addition(W, X, Y, Z):
    print("All the four values addition are: ", W + X + Y + Z)


s1 = 12.4
s2 = 3.5
s3 = 3
s4 = 7
addition(s1, s2, s3, s4)


# give all the types of datatype
def data(b1, b2, b3, b4):
    print(f"The values of {b1}, {b2}, {b3}, {b4} are: ", b1, b2, b3, b4)


a1 = 12
a2 = 12.4
a3 = [1, 3, 5, 6]
a4 = {"a": 1, "b": 5, "c": 4}

data(a1, a2, a3, a4)


# Same data type assign to variables
def learn(z1, b1):
    print("The Final value: ", z1 + b1)


list1 = ['a', 'b', 'c']
list2 = [1, 3, 2]
learn(list1, list2)


# Addition using for loop
def addval(n1, n2):
    print(f"values of {n1} and {n2}: ", n1 + n2)


list3 = [[4, 5], [6, 7], [5, 7]]
for val in list3:
    addval(val[0], val[1])
