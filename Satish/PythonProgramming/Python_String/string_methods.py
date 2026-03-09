#string methods
print(dir(str))

"""
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""

str1="we ARE learning PYTHON "
str1_lower=str1.lower()
print(str1_lower) # we are learning python
str1_upper=str1.upper()
print(str1_upper) # WE ARE LEARNING PYTHON

str1_title=str1.title()
print(str1_title) #We Are Learning Python

str1_capitalize=str1.capitalize()
print("cap",str1_capitalize)

str1_index=str1.index('A') # index start from 0
print(str1_index)

str1_count=str1.count('e')
print("count of e",str1_count)

str1_swapcase=str1.swapcase()
print(str1_swapcase)

str1_split=str1.split() # break string from space and give list
print(str1_split)

str1_strip=str1.strip()
print(str1_strip)

name="satish"
for ch in name:
    print(ch)

for index,ch in enumerate(name):
    print(index,ch)

print(enumerate(name))
print(list(enumerate(name)))

################################
#Q5 write a python program to convert odd length word in upper case and even length word in lower case.
str5 = "India iS BesT country in the world"
# output = "INDIA is best COUNTRY in THE WORLD"

word_lst=str5.split(" ")
print(word_lst)
output=""
for word in word_lst:
    if len(word)%2==0:
        output=output+word.lower()+ " "
    else:
        output = output + word.upper() + " "

print(output)

#Write a python program to get second largest word from goven string
str6="Everything is possible with hard work"

largest=0
second_largest=0
sec_largest_word=""
word_lst=str6.split()
for word in word_lst:
    if len(word)>largest:
        largest=len(word)
    elif len(word)>second_largest:
        second_largest=len(word)
        sec_largest_word=word

print(sec_largest_word)

