def add(a,b):
    print("Add",a+b)
add(5,6)
a1=5
b1=1
add(a1,b1)
add('hello','goodmorning')

l1=[1,2,3]
l2=[4,5,6]
add(l1,l2)
print('-'*50)
list2=[[5,9],[8,10],[11,12]]
for val in list2:
    add(val[0],val[1])

print('-'*50)

def mul(x,y=8):
    return x*y
result = mul(6)
print('Mul',result)
print('-'*50)

# args

def square_number(*args):
    print(args,type(args))
    for val in args:
        print(val,":",val**2)
        print(val,type(val))
square_number(2,3,4,5,5,6)

print("_"*50)
###############################################
# **kwargs parameter to the function.
def user_details(**kwargs):
    print(kwargs,type(kwargs))
    for k,v in kwargs.items():
        print(k,":",v)
user_details(name='janvika',age='6')

def verify_login(**kwargs):
    db_user = 'Janvika'
    db_password='12345'
    if kwargs['user_name']==db_user and kwargs['password']==db_password:
        print("login successfull")
    else:
        print("invalid login")
verify_login(user_name='Janvika',password='12345')
verify_login(user_name='pari',password='12345')

def fact(num):
    fact=1
    for i in range(num,0,-1):
        fact=fact*i
    return fact
result=fact(6)
print("factorial",result)
print("_"*50)

# return statement can stop the execution of the function

def get_add_of_number(num):
    add=0
    for i in range(num+1):
        if add>30:
            return add
        add=add+i
    print("Add value inside function:",add)
print(get_add_of_number(10))
print('_'*50)

def get_multiple_value(n1,n2,n3):
    add=n1+n2
    sub=n2-n3   
    mul=n3*n1
    return add,sub,mul
result=get_multiple_value(10,5,2)
print("Multiple value return:",result)
print("Add:",result[0],"sub:",result[1],"mul:",result[2])
print('_'*50)