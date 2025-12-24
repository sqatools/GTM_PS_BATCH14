# function without parameter
def greeting():
    print("Hello!")

greeting()
greeting()

# function with parameter
def greeting_msg(a):
    print("+" * 20)
    print(a)
    print("$"*20)

# Pass value to parameter
# 1. pass by value
greeting_msg("Welcome to Python Function")
# 2. pass by reference
x="Learning Python is fun"
y={'a': 123, 'b': 5678}
greeting_msg(a=x)
greeting_msg(y)
print("_"*50)
############################################
def addition(n1,n2):
    print(f"addition of {n1},{n2}:", n1+n2)
# pass by value
addition(30,50)
# pass by reference
m1=100
m2=500
addition(m1,m2)

l1=[3,5,6]
l2=['a','b','c']
addition(l1,l2)

print("_"*50)
############################################
# WAP to read list
list2=[[5,7],[4,8],[8,9]]
for val in list2:
    addition(val[0],val[1])
    print("_"*10)
print("_"*50)
############################################
# function with default parameter value

def multiplication(x,y=8):
    print(f"multiplication, x={x},y={y}:", x*y)
# call function with default value of y=8
multiplication(30)


