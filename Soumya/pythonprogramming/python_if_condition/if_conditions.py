a = 50
b = 50

print(a == b)

if a == b:
    print("a and b has equal value :", a, ",", b)
else:
    print("a and b has different value :", a, ",", b)

print("_" * 50)
# program to check the given number is odd or even
num1 = 12
if num1 % 2 == 0:
    print("This is even number :", num1)
else:
    print("This is odd number :", num1)

# print("This is even :", num1)


print("_" * 50)
########## if-elif-else #######

"""
if condi1:
   code1
elif cond2:
   code2
elif cond3:
   code3
else:
   else code
"""
n = 50
x = 40
y = 40
z = 30

if n == x:
    print("x and n has equal value:", x, n)
elif n == y:
    print("y and n has equal value", y, n)
elif n == z:
    print("z and n has equal value", z, n)
else:
    print("no one has matching value with n")

print("_" * 50)
m = 40
if m == x:
    print("x and m has equal value:", x, m)

if m == y:
    print("y and m has equal value", y, m)

if m == z:
    print("z and m has equal value", z, m)
else:
    print("z and m are not equal", z, m)

#######################
p = 40
print("value of P :", p)
p = 50
print("value of P :", p)

print("_" * 50)
##############################################
# Nested if condition
round1 = "pass"
round2 = "pass"
round3 = "pass"

if round1 == "pass":
    print("congrats 1st round is cleared")
    if round2 == "pass":
        print("congrats 2nd round is cleared")
        if round3 == "pass":
            print("congrats 3rd round is cleared")
        else:
            print("failed in 3rd round, try next time")
    else:
        print("failed in 2nd round, try next time")
else:
    print("failed in 1st round, try next time")

"""
AND Logic
cond1 and cond2
True and False : False
False and True : False
False and False : False
True and True : True


OR Logic
cond1 or cond2
True or False : True
False or True : True
False or False : False
True or True : True

> :  greater than
< :  less than
>= : greater equal
<= :  less than equal
is : is operator
is not: is not operator
in : in operator
not in : not in operator
"""

print("_" * 50)
#####################
"""
# write a python program to check the given number is divisible by 3 and 5
num1 = input("Please enter your value:")
# input accepts the values in string format only
print(num1, type(num1))
x = int(num1)

if x % 3 == 0 and x % 5 == 0:
    print("This number is divisible by 3 and 5 :", x)
else:
    print("This number is not divisible by 3 and 5 :", x)

print("_" * 50)
y = int(input("Please enter y value :"))
if y % 3 == 0 or y % 5 == 0:
    print("This number is divisible by 3 or 5 :", y)
else:
    print("This number is not divisible by 3 or 5 :", y)
"""

print("_" * 50)
##############################################
# write a program to accept the student marks and provides its result as marks obtained.
"""
marks = int(input("Please enter your marks:"))

if marks <= 30:
    print("Failed in Exam")
elif 30 < marks <= 40:   # chain action logic
    print("Pass with 3rd grade")
elif marks > 40 and marks <= 60:
    print("Pass with 2nd grade")
elif marks > 60 and marks <= 80:
    print("Pass with 1st Grade")
elif marks > 80 and marks <= 100:
    print("Pass with A++ Grade")
else:
    print("Marks should be less than 100")

"""
print("_"*50)
##############################
# write a python program to check given value is available in list of values.
val = 51
list1 = [5, 7, 9, 2, 50, 6]

if val in list1:
    print("number is available in the list:", val)
else:
    print("number is not available in the list", val)


print("_"*50)
# not in operator
tup1 = (5, 7, 9, 23)
n1 = 7
if n1 not in tup1:
    print("n1 is not available in the given tuple values")
else:
    print("n1 is available in the given tuple values")

print("_"*50)
##################
dict1 = {'a': 123, 'b': 456, 'c': 678}
val1 = 'a'
# Here we are checking for keys of the dict
if val1 in dict1:
    print("this val1 key is available in dict")
    print(dict1[val1], val1)
else:
    print("this val1 key is not available in dict")
    #print(dict1[val1])

print("_"*50)
##############################
# is operator

list1 = [5, 7, 8]
list2 = [5, 7, 8]
list3 = list1

# compare list1 with list2 using equal operator ==
if list1 == list2:
    print("Both are equal")
else:
    print("Both are not equal")


if list1 is list2:
    print("Both are equal using is")
else:
    print("Both are not equal using is")


print(list1 is list3) # True
print(list2 is list1) # False
print(list2 == list1) # True

#####################################
print("_"*50)
var = True

if var is True:
    print("variable has True value")
else:
    print("variable has False value")