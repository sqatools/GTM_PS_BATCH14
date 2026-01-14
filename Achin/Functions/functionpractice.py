#to take string as input and print 10 times
'''
def print_string(str1):
    for i in range(10):
        print(str1)
str1=input("Enter any string:")
print_string(str1)
'''
#to print a table of any number
'''
def print_table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
num=int(input("Enter any number to print its table:"))
print_table(num)
'''
#to find maximum of 3 numbers
'''
def maxof3nos(a,b,c):
    if(a>=b and a>=c):
        return a
    elif(b>=a and b>=c):
        return b
    else:
        return c
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
print("The maximum number is:",maxof3nos(a,b,c))
'''
#to find sum of elements in a list
'''
list1=[10,20,30,40,50]

def sumoflist(lst):
    sum=0
    for i in lst:
        sum+=i
    print(sum)

sumoflist(list1)

'''
#to find unique elements in a list
'''
list1=[1,2,3,4,5,6,7,8,9,10,5]
list2=[]

def uniquelist(lst):
    for i in lst:
        if i not in list2:
            list2.append(i)
    print(list2)
uniquelist(list1)
'''

