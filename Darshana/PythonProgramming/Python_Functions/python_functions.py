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

print("_"*50)
###############################################
# *args parameter to the function.

def get_square_of_values(*args):
    """
    *args accepts values in tuple format, user can provide n number of values with
    args parameter.
    :param args: this param accept n number value while
    :return:
    """
    print(args, type(args))
    for val in args:
        #print(val, ":", val**2)
        print(val, type(val))


get_square_of_values(4, 6, 7, 8, 12)
get_square_of_values(10, 20, 30)
get_square_of_values(5, 5.5, 'Python', [4, 5, 7], {'a': 123}, {5, 6, 73}, True)



print("_"*50)
###############################################
# **kwargs parameter to the function.

def user_details(**kwargs):
    """
    kwargs accepts the value in the key value and store as dictionary
    :param kwargs:
    :return:
    """
    print(kwargs, type(kwargs))

    for k, v in kwargs.items():
        print(k ,":", v)


user_details(name='Rahul', age=30, email='rahul@gmail.com', phone=5454655667)
#user_details(6, 7, 8, 9)


def verify_login(**kwargs):
    db_user = 'user1'
    db_pass = 'user@1234'
    if kwargs['username'] == db_user and kwargs['password'] == db_pass:
        print("Login Successful")
    else:
        print("Access denied")

print("_"*50)
#verify_login(username='user2', password='user@1234')
#verify_login(username='user1', password='user@1234')

#verify_login()

print("_"*50)
###########################################
# return statement in the function.

def get_factorial(num):
    fact = 1
    for i in range(num, 0,  -1):
        fact = fact*i

    return fact


result = get_factorial(6)
print("factorial result :", result)

# return statement can stop the execution of the function
def addition_of_values(num):
    add = 0
    for i in range(num):
        print(i)
        if add > 30:
               return add

        add = add + i

    print("Execution completed")


print("_"*50)
result_add = addition_of_values(20)
print("addition result :", result_add)



# return multiple values from function
def math_operations(n1, n2, n3):
    add = n1+n2
    mul = n2*n3
    sub = n3-n1
    return add, mul, sub

print("_"*50)
result = math_operations(10, 20, 30)
print("result :", result)  # (30, 600, 20)

a, b, c = math_operations(50, 100, 20)
print("addition :", a) # addition : 150
print("multiplication :", b) # multiplication : 2000
print("subtraction :", c) # subtraction : -30


def math_operation_With_kwargs(**kwargs):
    add = kwargs['n1'] + kwargs['n2']
    mul =  kwargs['n2'] *  kwargs['n3']
    sub =  kwargs['n3'] -  kwargs['n1']
    return add, mul, sub


p, q, r = math_operation_With_kwargs(n1=40, n2=60, n3=70)
print(p, q, r) # 100 4200 30