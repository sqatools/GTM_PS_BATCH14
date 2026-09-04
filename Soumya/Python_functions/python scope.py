"""
global variable: ->  when we declare any variable outside of the function, than it is called
                     global variable
                 -> If we want to define the global variable inside the function then we have to
                    user keyword  global.
                ->  we can change the3 global variable inside function with global keyword.
local variable :  ->  When we define variable inside function then that variable is called
                      local variable,
                -> its scope is limited to the function only. we can not access out side of the function.

nonlocal variable : -> when we define variable inside the outer function, then it becomes nonlocal variables
                    for inner functions.
"""


var_x = 200 # global variable
var_p = 0
def addition():
    global var_p, var_x
    var_x = 300
    var_p = 100
    var_y = 500 # local variable
    print("var_x :", var_x)
    print("addition :", var_x + var_y)

addition()

def multiplication():
    var_z = 40 # local variable
    print("var_p  global :", var_p)
    print("var_x :", var_x)
    print("multiply :", var_z*var_x)

print("_"*50)
multiplication()


############################## Non local variable #################################
var_A = 10 # global variable

def outer_function():
    var_B = 20 # non local variable

    def inner_fun1():
        nonlocal var_B
        var_C = 30 # local variable
        var_B = 50
        print("global var_A :", var_A)
        print("non local var_B :", var_B)
        print("local variable Var_C :", var_C)

    def inner_fun2():
        var_D = 40 # local variable
        print("global var_A :", var_A)
        print("non local var_B :", var_B)
        print("local variable Var_D :", var_D)


    inner_fun2()
    print("_" * 50)
    inner_fun1()
    print("_"*50)
    inner_fun2()

print("_"*50)
outer_function()

print("_"*50)
################### Function recursion ######
# when we call the  function inside the function, then it is called recursion.
def square(n):
    print(f"square of {n} :",n**2)
    if n == 1:
        return n
    square(n-1)


square(5)