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

def hello():
    print("Hello!")

#calling function
hello() # Hello!

print("_" * 50)


#############################
# function with parameter

def hello(name): # Here name is variable and called parameter of the function
    print(f"Hello! {name}")

hello('satish') #Hello! satish  (value 'satish' also called argument)


# Passing value to function parameters there are two way
#1. Pass By  value directly as shown above we have passed 'satish' as a value
# 2 Pass By reference

# In pass By reference we pass variable
x= 'Jyoti'
hello(x) #Hello! Jyoti


print("_"*50)
########################################
# function with default parameter value.

def multiplication(x,y=10):
    """
    This function accepting the default parameter value y=10
    if we want to overwrite the default value, then we have
    to assign new value while calling the function.
    ->  Default param will always on right side of the parameter list or end of parameters
    :param x:
    :param y:
    :return:
    """
    print(f"Multiplication of {x} and {y} is {x*y}")

# Call function with default value of y=10
multiplication(30) # 300

# Call function and change the default value y=30
# new value will overwrite default value of y
multiplication(30, 30) # 900

def addition(a,b,c=10,d=20):
    print(f"Addition of {a},{b},{c} & {d} is {a+b+c+d}")

addition(15,30) # Addition of 15,30,10 & 20 is 75


print("_"*50)
###############################################
# *args parameter to the function.

def get_square_values(*args):
    """
    *args accepts values in tuple format, user can provide n number of values with
    args parameter.
    :param args:
    :return:
    """
    for val in args:
        print(val,type(val))
    print(args,type(args)) #(5, 2.5, [1, 2, 3], {4, 5, 6}, True, 'satish', {'a': 123}, {8, 9, 7}) <class 'tuple'>

get_square_values(5,2.5,[1,2,3],{4,5,6},True,'satish',{'a':123},{7,8,9})

"""
5 <class 'int'>
2.5 <class 'float'>
[1, 2, 3] <class 'list'>
{4, 5, 6} <class 'set'>
True <class 'bool'>
satish <class 'str'>
{'a': 123} <class 'dict'>
{8, 9, 7} <class 'set'>
"""

print("_"*50)
###############################################
# **kwargs parameter to the function.

def user_details(**kwargs): # spell as Keyword arguments or kwargs
    """
     kwargs accepts the value in the key value and store as dictionary
    :param kwargs:
    :return:
    """
    print(kwargs['name'],kwargs['email'],kwargs['cell']) #satish satishpaliwal7172@gmail.com 7014755649
    for k,v in kwargs.items():
        print(f"Key is {k} and Value is {v}")
    print(kwargs,type(kwargs)) #{'name': 'satish', 'email': 'satishpaliwal7172@gmail.com', 'cell': 7014755649} <class 'dict'>

"""
Key is name and Value is satish
Key is email and Value is satishpaliwal7172@gmail.com
Key is cell and Value is 7014755649

"""

user_details(name='satish', email='satishpaliwal7172@gmail.com',cell=7014755649)

# MOST Note: when we call function they we don't put key in '' or "" string format but as kwargs accept value in dictionay so it put in ''

# Example Application of **kwargs

def verify_user_login(**kwargs):
    user_1='satish'
    password=12345
    if kwargs['user']==user_1 and kwargs['password']==password:
        print("Login Successful")
    else:
        print("Login Unsuccessful")


verify_user_login(user='satish',password=12345) #Login Successful

verify_user_login(user='satish',password=123) #Login Unsuccessful


print("_"*50)
###########################################
# return statement in the function.

# Find factorial of number e.g. fact(5)= 5*4*3*2*1

def get_factorial(number):
    fact=1
    for num in range(number,0,-1):
        fact=fact*num
    return fact

result=get_factorial(6)
print("result",result) #result 720


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
result_add = addition_of_values(10)
print("addition result :", result_add)

