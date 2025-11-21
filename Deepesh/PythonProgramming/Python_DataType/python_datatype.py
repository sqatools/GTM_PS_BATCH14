"""
Python data type.
1). Number
   i)  integer
   ii) float
   iii) complex

2). Sequential
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

print("_"*50)
################### Float ##############
"""
Properties:
1. Float is immutable data type. once it is defined can not update.
2. Float only contains whole number 0.0, 1.2 , 5667.678
3. There is no specific range for float data type.
"""

var1 =0.0
var2 = 5.6
var3 = 78978.4654654645
print("var1 :", var1, type(var1))  # 0.0 <class 'float'>
print("var2:", var2, type(var2))   # 5.6 <class 'float'>
print("var3 :", var3, type(var3))  # 78978.4654654645 <class 'float'>

print("_"*50)
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
print("real number :", p1.real) # 10.0
print("img number :", p1.imag) # 20.0

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
print("_"*15)
print("s2 :", s2, type(s2))
print("_"*15)
print("s3 :", s3, type(s3))
print("_"*15)
print("s4 :", s4, type(s4))
print("_"*15)
print("s5 :", s5, type(s5))
print("_"*15)
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
print(str10[-6]) # P
print(str10[2])  # t
print(str10[-4]) # t

print(str10[-2**2])# t : -4
print(str10[(-2)**2]) # o : 4
