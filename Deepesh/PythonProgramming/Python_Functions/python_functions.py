"""
def function_name():
    code
"""


# function is individual entity
# dir(list)

# when function is associated with class, then it becomes methods.
# list.append()

#############################
# function without parameter
def greeting():
    print("Good Morning")


# call the function
# greeting()
# greeting()
# greeting()

print("_" * 50)


#############################
# function with parameter
def greeting_msg(a):
    print("+" * 20)
    print(a)
    print("$" * 20)


# pass value to parameter
# 1. Pass by value
greeting_msg("Good Evening")

# 2. Pass by reference
x = "Learning Python is Fun"
y = {'a': 123, 'b': 5678}
greeting_msg(a=x)
greeting_msg(y)

print("_" * 50)


######################################
def addition(n1, n2):
    print(f"Addition of {n1}, {n2}:", n1 + n2)


# pass by value
addition(30, 50)  # Addition of 30, 50: 80

# pass by reference
m1 = 100
m2 = 500
addition(m1, m2)  # Addition of 100, 500: 600

l1 = [3, 5, 6]
l2 = ['a', 'b', 'c']
addition(l1, l2)  # Addition of [3, 5, 6], ['a', 'b', 'c']: [3, 5, 6, 'a', 'b', 'c']

print("_" * 50)
##########################################
# write a python program to read list
list2 = [[5, 7], [4, 8], [8, 9]]
for val in list2:
    addition(val[0], val[1])
    print("_" * 10)


# addition(40, 50, 60)
# TypeError: addition() takes 2 positional arguments but 3 were given

# addition(80)
# TypeError: addition() missing 1 required positional argument: 'n2'

print("_"*50)
########################################
# function with default parameter value.

def multiplication(x, y=8):
    """
    This function accepting the default parameter value y=8
    if we want to overwrite the default value, then we have
    to assign new value while calling the function.
    ->  Default param will always on right side of the parameter list or end of parameters
    :param x:
    :param y:
    :return:
    """
    print(f"Multiplication, x={x}, y={y}:", x * y)


# Call function with default value of y=8
multiplication(30)
# Multiplication, x=30, y=8: 240

# Call function and change the default value y=10
# new value will overwrite default value
multiplication(60, 10)
# Multiplication, x=60, y=10: 600


multiplication(2)
# Multiplication, x=2, y=8: 16
x = y = 8
multiplication(x, y)

def addition_values(A, B, C=30, D=50):
    print("addition :", A+B+C+D)

addition_values(10, 20)
# addition : 110

addition_values(A=20, B=50, D=70)
# addition : 170