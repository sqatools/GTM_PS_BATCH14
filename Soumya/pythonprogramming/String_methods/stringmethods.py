print(dir(str))
"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 
 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
  'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
   'partition', 'removeprefix', 'removesuffix', 'replace', 
   'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 
   'rstrip', 'split', 'splitlines', 'startswith', 'strip', 
   'swapcase', 'title', 'translate', 'upper', 'zfill'
"""
print("_"*50)
##########
# upper() and lower() method:
s1 = "Hello GooD MoRning"
print("lower case result :", s1.lower())  # hello good morning
print("upper case result :", s1.upper())  # HELLO GOOD MORNING

print("_"*50)
##########
# isupper() and islower() methods
s2 = "Python"
s3 = "PROGRAMMING"
s4 = "learning"
print("s2 is upper:", s2.isupper())  # s2 is upper: False
print("s3 is upper :", s3.isupper()) # s3 is upper : True
print("s4 is lower :", s4.islower()) # s4 is lower : True


print("_"*50)
##############
# swapcase() method :  method will convert upper to lower and lower to upper.
s5 = "WE are Learning Python"
print(s5.swapcase()) # we ARE lEARNING pYTHON

print("_"*50)
##############
# title() method : it will convert first letter of each word into capital case and remaining in small case.
s5 = "WE are leaRning PyThoN"
print("title output :", s5.title()) # We Are Learning Python
var = s5.title()
print("var:", var) # var: We Are Learning Python
print("s5 :", s5)  # WE are leaRning PyThoN

print("_"*50)
##############
# capitalize() method:  this method will convert first letter in capital and remaining in small case.
s6= "wE are leaRning PyThoN"
print(s6.capitalize())  # We are learning python


print("_"*50)
##############
# count() method : This method return the number of occurrences of any char or substring.
s7= "wE areG leaRning PyThoN Programming"
print("count of g :", s7.count('g')) # count of g : 3
print("counf of ing :", s7.count('ing')) # counf of ing : 2

print("_"*50)
##############
# index() method :  this method will return index of existing char/substring if it available
#                   else it will through error.
#                   ->  if char/sub string available multiple times, then it will return index first occurrences

s8 = "Learning Python is Fun P"
print("Index of P :", s8.index('P'))  # Index of P : 9

# print("Index of W :", s8.index('W'))
# ValueError: substring not found


print("_"*50)
##############
# find() method: find method will return index position of available char/substring and if target values is
# not available, then it will return -1
s9 = "Learning Python is Fun P"
print("index of is:", s9.find("is"))  # index of is: 16

# if target value is not available then it will return -1
print("index of are:", s9.find("are")) # index of are: -1


print("_"*50)
##############
# replace() method:
s9 = "Python Learning Python is Fun Python"
# replace all Python with Java
result = s9.replace("Python", "JAVA")
print("result :", result) # JAVA Learning JAVA is Fun JAVA

# replace Python with C++ from first 2 places
result2 = s9.replace("Python", "C++", 2)
print("result2 :", result2) # C++ Learning C++ is Fun Python

result3 = s9.replace("n", "N")
print("result3 :", result3) # PythoN LearNiNg PythoN is FuN PythoN

result4 = s9.replace("Python", "C++").replace("n", "m").upper()
print("result4 :", result4)  # C++ LEARMIMG C++ IS FUM C++


print("_"*50)
##############
# split() method: this method split string from given char/substring/special char and return list of words.

s10 = "nPython Learning Python is Fun Python"
result = s10.split(" ")
print("SPLIT result :", result)
# ['Python', 'Learning', 'Python', 'is', 'Fun', 'Python']

result2 = s10.split("n")
print("result2 :", result2)
# ['', 'Pytho', ' Lear', 'i', 'g Pytho', ' is Fu', ' Pytho', '']

result3 = s10.split("W")
print(result3)  # ['Python Learning Python is Fun Python']

print("_"*50)
################
# join method :  This method help to join the interable data with any char or special char.

str1 = "Hello"
r1 = "-".join(str1)  # H-e-l-l-o
print("result1 :", r1)

l1 = ['Hello', 'Good', 'Morning']
r2 = " ".join(l1)
print("result2 :", r2, type(r2))  # Hello Good Morning  # https://sqatools.in/python-string-methods/


print("_"*50)
################
# strip() method: this method remove trailing spaces.
s5 = "  Programming  "
print(s5)
print(s5.strip())  # Programming  # remove both side sapces
print(s5.lstrip()) # remove left side space
print(s5.rstrip()) # remove right side space

print("_"*50)
#################
str_b = "345678879"
str_c = "Hello 768789"
str_d = "Python123"
str_e = "GoodMorning"

print("str_b is contains number :", str_b.isnumeric()) # True
print("str_d is contains alpha number :", str_d.isalnum()) # True
print("str_c is contains only alpha:", str_c.isalpha()) #  False
print("str_e is contains only alpha:", str_e.isalpha()) #  True




