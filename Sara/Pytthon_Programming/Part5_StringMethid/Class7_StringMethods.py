print(dir(str)) # dir gives list of method available in a particular class (e.g. str).

# for user specfic method there is no underscore.
# the method with underscore are automatically used by python in backend.
'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', 
'__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode',
'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

'''
print()
###################################################
print("-"*15, "Upper and Lower Method","-"*15)
s1="We are LeARniNg PYthon"
print("All in upper case: ", s1.upper()) # All in upper case:  WE ARE LEARNING PYTHON
print("All in lower case: ", s1.lower()) # All in lower case:  we are learning python

print()
###################################################
print("-"*15, "isupper and islower Method","-"*15)
a1="PYTHON"
a2="morning"
a3="learning"
a4="PyThon"
print(" a1=PYTHON is upper case: ", a1.isupper()) # True
print(" a2=morning is lower case: ", a2.islower()) # True
print(" a3=learning is upper case: ", a3.isupper()) # False
print(" a4=PyThon is upper case: ", a4.isupper()) #False

print()
###################################################
print("-"*15, "swapcase Method","-"*15)
e1="Really Really excited"
print(e1.swapcase()) # rEALLY rEALLY EXCITED

print()
##############################################
print("-"*15, "title Method","-"*15)
e1="REALLY Really eXcited"
print(e1.title()) #Really Really Excited

print()
##############################################
print("-"*15, "capitalize Method","-"*15)
e1="REALLY Really eXcited"
print(e1.capitalize()) # Really really excited

print()
##############################################
print("-"*15, "count Method","-"*15)
e1="REALLY Really eXcited"
print(e1.count('R')) # 2
print(e1.count('E')) # 1
print(e1.count('e')) # 3

print()
##############################################
print("-"*15, "index Method","-"*15)
e1="REALLY Really eXcited"
print(e1.index('t')) # 18
print(e1.index('l')) # 10 (will print the first index only if we have more than once
#print(e1.index("W")) # # not print anything coz there is no such char in string
print(e1.index('Rea')) # 7

print()
##############################################
print("-"*15, "find Method","-"*15)
e1="REALLY Really eXcited"
print(e1.find('l')) # 10
print(e1.find('lly')) # 10
print(e1.find('w')) # -1

print()
##############################################
print("-"*15, "replace Method","-"*15)
e1="REALLY Really Really eXcited"
print(e1.replace('Really', 'Hello')) # REALLY Hello Hello eXcited
print(e1.replace('Really','Yo',1)) # REALLY Yo Really eXcited

print()
##############################################
print("-"*15, "spliy Method","-"*15)
e1="REALLY Really Really eXcited"
print(e1.split(" ")) # ['REALLY', 'Really', 'Really', 'eXcited']
print(e1.split("e")) # ['REALLY R', 'ally R', 'ally ', 'Xcit', 'd']
print(e1.split('w')) # ['REALLY Really Really eXcited'] (since there is no w, it will consider entire string as 1 list value)

print()
##############################################
print("-"*15, "split Method","-"*15)
e1="  World  "
print(e1.strip()) # will remove spaces from start and end
print(e1.lstrip()) # will remove spaces from start i.e. from left
print(e1.rstrip()) # will remove spaces from end i.e. from right

print()
##############################################
print("-"*15, "isalpha, isnum and isalphanum Method","-"*15)
e1= "12345"
e2="Hello"
e3="34Hello00"
e4="34Hello00"
e5= "Good Morning"
e6= "Good Morning"
print(e1.isnumeric()) #True
print(e2.isalpha()) #True
print(e3.isalnum()) #True
print(e4.isnumeric()) #False
print(e5.isalpha()) #False
print(e6.isalnum()) #False

print()
##############################################
print("-"*15, "join Method","-"*15)
e1="World"
print(("*").join(e1)) # W*o*r*l*d

e2=['1','Hello','33ee']
print((" ").join(e2)) # 1 Hello 33ee
print(("+").join(e2)) # 1+Hello+33ee