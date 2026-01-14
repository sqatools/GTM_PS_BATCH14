#print(dir(str))

"""
print(dir(str))
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
  'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
   'swapcase', 'title', 'translate', 'upper', 'zfill']
"""
print("_"*50)
##############
#swapcase() method:Method will convert upper to lower and lower to upper
s5="WE are Learning Python"
print(s5.swapcase())

print("_"*50)
##############
#title() method: It will convert the 1st letter of the word to Capital
s5="WE are Learning Python"
print(s5.title())    #We Are Learning Python

print("_"*50)
##############
# Capitalize method: this method will convert first letter in capital
s5="wE are Learning Python"
print(s5.capitalize())

print("_"*50)
##############
#count()



print("_"*50)
##############
# index() method : this method will return index of character.

s8="Learning pytho nis Fun"
print("index of p: ",s8.index('p'))
#print("index of w: ",s8.index('w'))  ValueError: substring not found

print("_"*50)
##############
#find() method: find method will return index position of char/subsvtring
# not availabe , then it will return -1

s9="Learning python is fun P"
print()
