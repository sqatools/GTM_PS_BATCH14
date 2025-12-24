"""
global variable: ->  when we declare any variable outside of the function, then it is called
                     global variable
                 -> If we want to define (declare new variable as global) the global variable inside the function then we have to
                    use keyword  global.
                ->  If we want to change the value of global variable value inside the function then we first define global variable inside function with global keyword and then can assign new value to it..
local variable :  ->  When we define variable inside function then that variable is called
                      local variable,
                -> its scope is limited to the function only. we can not access out side of the function.

nonlocal variable : -> when we define variable inside the outer function, then it becomes nonlocal variables
                    for inner functions.

"""

x="Good Morning!" # This is a global variable because it is declared outside of all functions

def first():
    y='welcome' # Local variable
    print(x) #Good Morning!
    print(y) #welcome

def second():
    print(x) #Good Morning!

first()
second()

# Now if we want to change value of x inside function then we have to define x with global keyword first then assign new value to it

def third():
    #global x
    x="hello"
    print(x)

third()

a=70 # Global variable
def outer_function():
    p=50 # nonlocal variable
    def inner_function():
        q=30 # local variable

print("_"*50)
################### Function recursion ######
# when we call the  function inside the function, then it is called recursion.
def square(n):
    print(f"square of {n} :",n**2)
    if n == 1:
        return n
    square(n-1)


square(5)