"""
Python data type.
1). Number
   i)  integer
   ii) float
   iii) complex

2). Sequential : This family data type will follow positive and negative indexing.
   i). String
   ii). List
   iii). Tuple

3). Dictionary
4). set
5). Boolean
"""

################### Integer ##############
"""
Properties:
1. Integer is immutable data type. once it is defined can not update.
2. Integer only contains whole number , 1, 3, 45, 789.
3. There is no specific range for integer data type.
"""
n1 = 0
n2 = 1
n3 = 7878798798
n4 = 878970870889798798078787
# n5 = 78.89 | not int
print("n1 :", n1, type(n1))  # 0 <class 'int'>
print("n2 :", n2, type(n2))  # 1 <class 'int'>
print("n3 :", n3, type(n3))  # 7878798798 <class 'int'>
print("n4 :", n4, type(n4))  # 878970870889798798078787 <class 'int'>

print("_" * 50)
################### Float ##############
"""
Properties:
1. Float is immutable data type. once it is defined can not update.
2. Float only contains whole number 0.0, 1.2 , 5667.678
3. There is no specific range for float data type.
"""

var1 = 0.0
var2 = 5.6
var3 = 78978.4654654645
print("var1 :", var1, type(var1))  # 0.0 <class 'float'>
print("var2:", var2, type(var2))  # 5.6 <class 'float'>
print("var3 :", var3, type(var3))  # 78978.4654654645 <class 'float'>

print("_" * 50)
################### Complex ##############
"""
Properties:
1. Complex datatype is immutable data type. once it is defined can not update.
2. Complex datatype is combination of real and imaginary value.
3. Format to define the complex number is  x+yj
4. Complex number generally we use for scientific calculation.
"""

p1 = 10 + 20j
# 10 : real number
# 20 : imaginary number
print("p1 :", p1, type(p1))  # (10+20j) <class 'complex'>
print("real number :", p1.real)  # 10.0
print("img number :", p1.imag)  # 20.0

p2 = 40 + 50j
print(p2)

############################Sequential data type ############

###
# string datatype:
"""
Properties:
-> String is immutable data type, can not the value.
-> We can defined string with single quote, double quote, triple quote.
-> String follow positive negative indexing for each character in the string.
-> There is no specific limit to define the string.
"""

s1 = ""
s2 = 'Hello'
s3 = "H"

s4 = """
Copilot Search Branding
Global web icon
Cricbuzz
https://www.cricbuzz.com
"""

s5 = '''
2 days ago · Check live cricket scores,
 upcoming cricket matches, ball-by-ball commentary,
  & live score updates with latest news for today's
   live cricket matches on ESPNcricinfo.
'''

s6 = "We are learning Python Programming"

print("s1 :", s1, type(s1))
print("_" * 15)
print("s2 :", s2, type(s2))
print("_" * 15)
print("s3 :", s3, type(s3))
print("_" * 15)
print("s4 :", s4, type(s4))
print("_" * 15)
print("s5 :", s5, type(s5))
print("_" * 15)
print("s6 :", s6, type(s6))

s7 = "ello, we are 6768766 &*&*(&( ##%$# learning Python " \
     "ProgrammingVery good evening"

print("s7 :", s7, type(s7))
# Hello, we are learning Python ProgrammingVery good evening

s8 = "My teacher's"
s9 = 'Learning "Python" Programming'
print("s8 :", s8)  # My teacher's
print("s9 :", s9)  # Learning "Python" Programming

abc = "Hello"
abc = "Python"
print(abc)

############### String follows positive negative indexing #########

str10 = "Python"

"""
  0  1  2  3  4  5    +ve indexing
  P  y  t  h  o  n
 -6  -5 -4 -3 -2 -1   -ve indexing
"""

print(str10[0])  # P
print(str10[-6])  # P
print(str10[2])  # t
print(str10[-4])  # t

print(str10[-2 ** 2])  # t : -4
print(str10[(-2) ** 2])  # o : 4

print("_"*50)
############################### list ####################
"""
# Properties:
-> List is mutable data type, that we can modify any point of time.
-> List can contains any types of data, int, float, complex, str, list, tuple, dict, set, boolean.
-> List follows positive negative indexing as like.
-> We define list with square bracket.
"""

list1 = [2, 3.7, 3+30j, 'Hello', [3, 5, 6], (1, 5, 7), {'a': 123}, {5, 7, 8}, True]

print(list1, type(list1))
# [2, 3.7, (3+30j), 'Hello', [3, 5, 6], (1, 5, 7), {'a': 123}, {8, 5, 7}, True] <class 'list'>

#        0  1  2  3   4
list2 = [4, 7, 8, 12, 56]
#       -5  -4 -3 -2  -1

print(list2[2])  # 8
print(list2[-1]) # 56

print("_"*50)
list3 = [2, 3.7, 3+30j, 'Hello', [3, 5, 6], (1, 5, 7), {'a': 123}, {5, 7, 8}, True]
print(list3[4])  # [3, 5, 6]
print(list3[4][1])  # 5

print(list3[2]) # (3+30j)
print(list3.index(True)) # 8


list4 = [6, 8, 9]
list4.append(100)
print("list4 :", list4)
# list4 : [6, 8, 9, 100]

print("_"*50)
######################### Tuple ####################
"""
# Properties:
-> Tuple is immutable data type, that we can not modify.
-> Tuple can contains any types of data, int, float, complex, str, list, tuple, dict, set, boolean.
-> Tuple follows positive negative indexing as like.
-> We define tuple with round bracket. e.g. tup1 = (4, 6, 8)
"""

tup1 = (2, 3.5, 2+3j, 'Python', [3, 6, 8], (1, 3, 5), {'a': 456}, {4, 7, 8}, False, "Yesterday's")

print(tup1, type(tup1))
# (2, 3.5, (2+3j), 'Python', [3, 6, 8], (1, 3, 5), {'a': 456}, {8, 4, 7}, False) <class 'tuple'>

# get python from tup1
print(tup1[3]) # Python

print(tup1[-3]) # {'a': 456}

print(tup1[-1]) # Yesterday's

print(tup1[-3+1]) # False


print("_"*50)
######################### Dictionary ####################
"""
# Properties:
-> Dictionary is mutable data type, we can modify the data at any point of time.
-> Dictionary contains data in keys value pair , e.g  {'key1': 'value1', 'key2': 'value2'}
-> Dictionary allows unique keys only, duplicate keys are not allowed.
   e.g.  {'a': 123, 'b': 567, 'c': 789, 'a': 500}
   -> if user provide duplicate key, then it will consider the latest defined value.
-> Dictionary follows LIFO (last in first out)

-> Dictionary allows only immutable data type as key, e.g. int, float, complex, str, tuple, boolean.
-> There is no restriction of value of the dict data type.
"""


dict1 = {'a': 123, 5: 'Python', 3.5: [3, 5, 7]}
print(dict1, type(dict1))
# {'a': 123, 5: 'Python', 3.5: [3, 5, 7]}  <class 'dict'>

# get value from dict with the help of key
print(dict1['a']) # 123

# update existing key data
dict1['a'] = 500
# Add new key value
dict1['b'] = 200

print("dict1 :", dict1)
# {'a': 500, 5: 'Python', 3.5: [3, 5, 7], 'b': 200}

dict2 = {100: 'Hello',
         5.5 : [3, 5, 7],
         45+5j: (6, 9, 0),
         'abc': {'a': 123, 'b': 678},
         (1, 2, 3): {5, 8, 9, 12, 5},
         True: 345,
          # [4, 6, 7] : 7567  # TypeError: unhashable type: 'list'
         }

print(dict2)
# {100: 'Hello', 5.5: [3, 5, 7], (45+5j): (6, 9, 0), 'abc': {'a': 123, 'b': 678}, (1, 2, 3): {8, 9, 12, 5}, True: 345}


print("_"*50)
######################### set data type ####################
"""
# Properties:
-> Set is mutable data type, we can modify it at any point of time.
-> Set store value in curly bracket.
-> Set only allows immutable type as member, int, float, complex, string, tuple, boolean.
-> Set only contains unique values, duplicate values are not allowed.
-> Set store values in random order. 
"""

set1 = {12, 13, 12, 5, 'Python', (4, 6, 8), True, 5.7, 7+34j, 5}
print(set1, type(set1))
# {True, 5, 5.7, (4, 6, 8), 12, 13, (7+34j), 'Python'} <class 'set'>

#set2 = {12, 13, 5, 'Python', (4, 6, 8), True, 5.7, 7+34j, 5, {3, 5, 7}}
#print(set2)
# TypeError: unhashable type: 'list'
# TypeError: unhashable type: 'set'

print("_"*50)
######################### Boolean ####################
"""
Properties:
-> boolean has 2 values True and False
-> Boolean is immutable data type.
-> Boolean is output of any of the condition.
"""
a = 30
b = 50
c = 30
print(a == b) # False
print(a == c) # True





