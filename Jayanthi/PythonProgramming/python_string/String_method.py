# len(): Returns the length of a string. Here’s an example:

str1="Python Programming"
str2= len(str1)
print("Length of the",str1,"is",str2)
print("-"*50)

# lower(): Converts all characters in a string to lowercase. Here’s an example:
str3=str1.lower()
print("Lower case od string",str3)
print("-"*50)

# upper(): Converts all characters in a string to uppercase. Here’s an example:
str4=str1.upper()
print("upper case od string",str4)
print("-"*50)

# title(): Capitalizes the first character of each word in a string. Here’s an example:
str5=str1.title()
print("Title of the string",str5)
print("-"*50)

# capitalize(): Capitalizes the first character of a string. Here’s an example:
str6=str1.capitalize()
print("capitalize of the string",str6)
print("-"*50)

# swapcase(): Swaps the case of all characters in a string. Here’s an example:
str7=str1.swapcase()
print("Swapcase of the string",str7)
print("-"*50)

# count(): Returns the number of occurrences of a substring in a string.
str8=str1.count('n')
print("Count of n:",str8)
print("-"*50)

# find(): Returns the index of the first occurrence of a substring in a string.
str9=str1.find('n')
print("find of n:",str9)
print("-"*50)

# rfind(): Returns the index of the last occurrence of a substring in a string.
str10=str1.rfind('n')
print("find of r'n':",str10)
print("-"*50)

# index(): Like `find()`, but raises a `ValueError` if the substring is not found.
str11=str1.index('n')
print("index of 'n':",str11)
print("-"*50)

# rindex(): Like `rfind()`, but raises a `ValueError` if the substring is not found.
str12=str1.rindex('n')
print("index of r'n':",str12)
print("-"*50)

# startswith(): Returns `True` if a string starts with a specified prefix, otherwise `False`.
str13= str1.startswith('Python')
print("starts with programming':",str13)
print("-"*50)

# endswith(): Returns `True` if a string ends with a specified suffix, otherwise `False`.
str14= str1.endswith('Programming')
print("end with programming':",str14)
print("-"*50)

# replace(): Replaces all occurrences of a substring with another substring.
str15=str1.replace('Python','Java')
print("Replace with String:",str15)
print(""*50)

# strip(): Removes whitespace (or other characters) from the beginning and end of a string.
str="     Python Programming     "
str16=str.strip()
print("Both space removed:",str16)

# rstrip(): Removes whitespace (or other characters) from the end of a string.
str17=str.rstrip()
print("end space removed:",str17)

# lstrip(): Removes whitespace (or other characters) from the beginning of a string.
str18=str.lstrip()
print("end space removed:",str18)

# split(): Splits a string into a list of substrings using a specified delimiter.
str19=str.split('n')
print("Splitted the string",str19)

# rsplit(): Splits a string from the right into a list of substrings using a specified delimiter.
str20=str.rsplit('n')
print("Splitted the string",str20)

# join(): Joins a list of strings into a single string using a specified delimiter
a=['world','joy','jesus']
str20=" ".join(a)
print(str20)











