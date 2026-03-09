print("Hello World")

a= b=c= 10
print(a, b, c)

a, b, c=10, 20, 30
print(a, id(a))
print(b, id(b))
print(c, id(c))

print("*"*70)
print("addition of 3 numbers is:", a+b+c)
print("subtraction of 3 numbers is:", a-b-c)
print("multiplication 3 numbers is:", a*b*c)
print("division of 2 numbers is:", a/b)
print("division of 2 numbers is:", a//b)
print("square root of two numbers", a**2)
print("cube root of two numbers", a**3)

v1=15
print(v1%3)
print(v1%4)

i=10
j=30
k=10
print(i==j)
print(i==k)
print(i!=j)

s1=("hello")
print(s1*5)

print(i, j)
print(i, end=" ")
print(j, end=" ")

V1=10

print("*"*70)
username = "Mohan"
age = 29
city = "Mumbai"
# My name is Mohan and age is 29 and living in mumbai
print("my name is" ,username, "and age is", age, "and living in",city)

print("*"*70)
# (a+b)^2 = a^2 + b^2 + 2ab
a=10
b=20
ls=(a+b)**2
ls1=(a**2)+(b**2)+2*a*b
print(ls==ls1)

#numbers---->integer, float, complex
#sequential----string, list, tuple
#dictionary
#boolean
#set

n1=10
n2=100000983898763
n1=20
f=10.0
f1=1999999999999999.789987654567
print(n1, type(n1))
print(f1, type(f1))
print(n2)

c=10+20j
print(c, type(c))
print("real", c.real)
print("imaginary", c.imag)


list3 = [2, 3.7, 3+30j, 'Hello', [3, 5, 6], (1, 5, 7), {'a': 123}, {5, 7, 8}, True]
print(list3[4])  # [3, 5, 6]
print(list3[4][1])  # 5

print(list3[2]) # (3+30j)
print(list3.index(True)) # 8

# program to check the given number is odd or even
"""


num1 = int(input("Enter a number"))
if num1%2==0:
    print("This is even number :", num1)
else:
    print("This is odd number :", num1)

"""
print("*"*70)
val=10
list1 = [5, 7, 9, 2, 50, 6]
if val in list1:
    print("number is available in the list:", val)
else:
    print("number is not available in the list", val)



print("_"*40)
# No output with range if values are not in range
for i in range(10, 1, 1):
    print(i)

print("_"*40)
for i in range(6, 1, -1):
    for j in range(i, 1, -1):
        print("*", end=" ")
    print()

print("_"*40)
for i in range(1, 6):
    for j in range (1,1+i):#(1,2)
        print("*", end=" ")
    print()

print("_"*40)
for i in range(1, 8):
    for j in range (1, 6):
        if j!=2 and j!=3 and j!=4 :
            print("*", end=" ")

    print()


str1 = "Hello we Are Learning Python"
# expected output1 =

# empty dict variable
output1 = {}
# split to get list of words
word_list = str1.split(" ") # ['Hello', 'we', 'Are', 'Learning', 'Python']
print(word_list)

for word in word_list: # Hello
    f_char = word[0]
    f_char1 = word[-1]
    f_char2 = f_char+f_char1
    output1[f_char2] = word

print("output1 :", output1)



