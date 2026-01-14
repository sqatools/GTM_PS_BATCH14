from Swital.Python_String.SOA_Site_String_Programs import count


def greeting():
    print("Good Morning")
greeting()
greeting()
greeting()

def greeting(a):
    print(a)
greeting(10)
greeting(11)
greeting("test")

#1). Python function program to add two numbers.
"""
print("_"*50)
def addition(n1,n2):
    print(n1+n2)
n1=int(input("Enter a number"))
n2=int(input("Enter another number"))
addition(n1,n2)
"""


#2). Python function program to print the input string 10 times.
"""
print("_"*50)
def string123(str):
    print(str*10)
string=input("Enter a string")
string123(string)
"""

#3). Python function program to print a table of a given number. i*num=a
"""
print("_"*50)
num=int(input("Enter a number"))
def table(num):
    a=0
    for i in range(1, 11):
        a=i*num
        print(i, "*", num, "=", a)
table(num)
"""

#4). Python function program to find the maximum of three numbers.
"""

Input: 17, 21, -9
Output: 21


def maximum(num1,num2,num3):
    if num1>num2 and num1>num3:
        print("maxminum number is:", num1)
    if num2>num3 and num2>num1:
        print("maxminum number is:", num2)
    if num3>num2 and num3>num1:
        print("maxminum number is:", num3)
num1=int(input("Enter a number"))
num2=int(input("Enter another number"))
num3=int(input("Enter another number"))
maximum(num1,num2,num3)

"""

#5). Python function program to find the sum of all the numbers in a list.
"""
Input : [6,9,4,5,3]
Output: 27

print("_"*50)
l = [6,9,4,5,3, 7]
def total(l):
    for val in l:
        t=0
        t += val
    print("Sum of given list: ",t)
total(l)

"""


#6). Python function program to multiply all the numbers in a list.
"""
Input : [-8, 6, 1, 9, 2]
Output: -864

print("_"*50)
def mul(list1):
    t = 1
    for val in list1:
        t *= val
    print("Product of elements in the given list: ",t)
list1 = [-8, 6, 1, 9, 2]
mul(list1)

"""

#7). Python function program to reverse a string.
"""
Input: Python1234
Output: 4321nohtyp


print("_"*50)
string=input("Enter a string")
def reverse(string):
    a=string[::-1]
    print(a)
reverse(string)


"""
#8). Python function program to check whether a number is in a given range.
"""
Input : num = 7, range = 2 to 20
Output: 7 is in the range


print("_"*50)
num=int(input("Enter a number"))
def rangeCheck(num):
    if num in range(2, 20):
        print(num, "is in a given range: ", num)
    else:
        print(num, "is not in a given range: ", num)
rangeCheck(num)

"""

#9). Python function program that takes a list and returns a new list with unique elements of the first list.
"""
Input : [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
Output : [2, 3, 1, 4, 6 ]


print("_"*50)
def unique(list1):
    print(list(set(list1)))
list1 = [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
unique(list1)

"""

"""
10). Python function program that take a number as a parameter and checks whether the number is prime or not.
Input : 7
Output : True


print("_"*50)
num1 = int(input("Enter a number"))
def prime(num1):
    count = 0
    for i in range(2,num1):
        if num1% i == 0:
           count += 1
    if count>0:
        print(num1, "is nOt a prime number")
    else:
         print(num1, "is a prime number")
prime(num1)

"""

#11). Python function program to find the even numbers from a given list.
"""
Input : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Output : [2, 4, 6, 8]


print("_"*50)
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even_odd(list1):
    even_odd_list = []
    for num in list1:
         if num%2==0:
            even_odd_list.append(num)
    print(even_odd_list)
even_odd(list1)

"""

str1 = "Hello we Are Learning Python"
# expected output1 = {'H': 'Hello', 'w': 'we', 'A': 'Are', 'L': 'Learning', 'P': 'Python'}
output={}
word_list=str1.split(" ")
print(word_list)
for word in word_list:
    ch=word[0]
    output[ch]=word
print(output)

#######################################################################
#Home Work str2 = "Hello we Are Learning Python"
# expected output1 = {'Ho': 'Hello', 'we': 'we', 'Ae': 'Are', 'Lg': 'Learning', 'Pn': 'Python'}

print("_"*50)
str2 = "Hello we Are Learning Python"
output1={}
word_list1=str2.split(" ")
print(word_list)
for word in word_list1:
    ch1=word[0]
    ch2=word[-1]
    ch3=ch1+ch2
    output1[ch3]=word
print(output1)

print("_"*50)
price_dict = {'Apple': 50, 'Banana': 60, 'Mango': 200, 'watermelon': 300}
item_purchased = {'Apple': 5, 'Banana': 15, 'Mango': 5, 'watermelon': 2}

fruit_bill_dict = {}
total_bill = 0
for fruit, price in price_dict.items():
    # get fruit name
    print("fruit_name :", fruit)
    # get fruit price
    print("fruit_price :", price)
    # get fruit purchased
    print("fruit purchased :", item_purchased[fruit])
    fruit_bill = price * item_purchased[fruit]
    fruit_bill_dict[fruit] = fruit_bill
    print("Fruit bill :", fruit_bill)
    # get total bill
    total_bill = total_bill + fruit_bill

    print("_" * 20)

print("Total fruit bill :", total_bill)  # Total fruit bill : 2750
print("Fruit bill data :", fruit_bill_dict)
