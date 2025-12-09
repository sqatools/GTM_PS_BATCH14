#q1 :  write a python program to count total vowels from given string.
str1 = "Hello we are LeArning PythOn"
vowels = "aeiou"
count = 0
for char in str1:
    if char.lower() in vowels:
        count += 1
    else:
        continue

print("total vowels :", count)


print("#"*50)
#q2 :  write a python program remove duplicate character from given string and generate output.
str2 = "Hello we are LeArning PythOn"
output = "" #Helo warLAni...

for char in str2:
    if char not in output:
        output = output + char
    else:
        continue

print("output :", output)


print("#"*50)
############################################
#q3 :  write a python program remove duplicate words from given string and generate output.
str3 = "Mona Pavan Achin Anshika Pavan Achin Mona"
output = "" #Mona Pavan Achin Anshika
word_list = str3.split(" ")
print(word_list)

for word in word_list:
    if word not in output:
        output = output + word + " "
    else:
        continue

print("output :", output) # Mona Pavan Achin Anshika

# 2nd approach
# convert word into set, that will remove duplicate name
set_result = set(word_list)
# join the set words with space using join method
output = " ".join(set_result)
print("output :", output) # Mona Anshika Achin Pavan


print("#"*50)
############################################
#q4 :  write a python program get largest word from given string.

str4 = "We Are Learning Python Programming and its Fun"
word_list = str4.split(" ")
print(word_list)
largst_word = ""
largst_len = 0

for word in word_list:
    if len(word) > largst_len: # 3 > 2 | 8 > 3 | 6 > 8 | 11 > 8
        largst_len = len(word) # 2, 3, 8, 11
        largst_word = word # We, Are, Learning, Programming
    else:
        continue

print("Largest word and largest len:", largst_word, largst_len)
# Programming 11


################################
#Q5 write a python program to convert odd length word in upper case and even length word in lower case.
str5 = "India iS BesT country in the world"
# output = "INDIA is best COUNTRY in THE WORLD"
#
# """
Properties:
-> String is immutable data type, can not update the value.
-> We can define string with single quote, double quote, triple quote.
-> String follow positive negative indexing for each character in the string.
-> There is no specific limit to define the string.
"""
str1 = 'Hello'
str2 = "We are learning Python"
str3 = '''
Zorzi is down on the ground clutching his right hamstring. 
He turned for the second run and immediately felt something, 
managed to hobble to the other end.
'''

str4 = """
He turned for the second run and immediately felt something,
 managed to hobble to the other end. This does not look good.
The physio is out there in the middle. de Zorzi is in a lot 
of pain. Meanwhile, Maharaj is ready near the rope 
"""

print(str1, type(str1))
print("_"*50)
print(str2, type(str2))
print("_"*50)
print(str3, type(str3))
print("_"*50)
print(str4, type(str4))
print("_"*50)

#################### string follows positive and negative indexing #######

str_a = "Python"

"""
 0  1  2  3  4  5   +ve indexing
 P  y  t  h  o  n
-6 -5 -4 -3 -2 -1   -ve indexing
"""

print(str_a[0])  # P
print(str_a[-3]) # h

print("index of t :", str_a.index('t')) # index of t : 2

print("_"*50)
################################## string formatting ####################

name = "Rahul"
age = 25
city = "Mumbai"

# name = input("Please enter username :")
# age = input("Please enter age:")  # "25"
# city = input("Please enter city name:")

# My name is Rahul and age is 25, I live in mumbai

# 1. string concatenation:
result1 = "My name is "+name+" and age is "+str(age)+", I live in "+city
print("Result1 :", result1)


# 2. string format method:
result2 = "My name is {} and age is {}, I live in {}".format(name, age, city)
print("Result2 :", result2)

# 3. f string formatting:
result3 = f"My name is {name} and age is {age}, I live in {city}"
print("Result3 :", result3)

print("_"*50)
#################### convert string into raw string #########
# \t : add space in string
# \n :  add next line in string.

str_b = r"Hello \t\t we are \n Learning Python"
print(str_b)  # Hello \t\t we are \n Learning Python

str_c = r"c:\nov\tools"
print(str_c)  # c:\nov\tools

print("_"*50)
############################# Slicing #############
# Rule1 : str[start index:  end index]
"""
->  In this rule it will always get output from left to right.
->  default start index value is 0
->  default end index value is end of string.
->  start index and end index could be positive negative.
->  Output will include the start index value and exclude end index value
"""

str_d = "Python Programming"
print(str_d[0:6]) # Python
print(str_d[-11:-1]) # Programmin

# consider default end value
print(str_d[-11:])  # Programming
print(str_d[0:-11]) # Python
print(str_d[-15:-11]) # hon
print(str_d[0:10]) # Python Pro


print("_"*50)
# Rule2 : str[start index:  end index: step value]
"""
-> In this rule, output will include start index value and exclude end index value
-> default start index is zero (0) if step value is +ve
-> default start index is -1 if step value is -ve
-> default end index will be end of string if step value is +ve
-> default end index will be start of string if step value is -ve
"""

s1 = "Learning Python If fun"
print(s1[0:5:1]) # Learn
# get alternate characters
print(s1[0:22:2]) # Lann yhnI u

# default start value as zero as step value is +ve
print(s1[:11:1])  # Learning Py

# default start value as -1 as step value is -ve
print(s1[:11:-1])

# default end index will be end of string if step value is +ve
print(s1[2::1])  # arning Python If fun

#  default end index will be start of string if step value is -ve
print(s1[-7::-1]) # nohtyP gninraeL
print(s1[7::-1]) # gninraeL

# reverse the entire string
s2 = "Good Morning"
print(s2[::-1]) # gninroM dooG
print(s2[-1:-len(s2)-1:-1])  # gninroM dooG

print(s2[::1])  # Good Morning

# print all the character except first and last
print(s2[1:-1]) # ood Mornin

# Homework slicing
str3 = "Virat is Best Batsman of India"
# output1 = "VViratt iiss BBestt BBatsmann ooff IIndiaa"
# output2 = "airat is Best Batsman of IndiV"
# output3 = "tiraV si tesB natsmaB fo andiI"




print("_"*50)
################ Apply loop on string ###############
str10 = "Learning Python"

# loop without indexing
for char in str10:
    print(char)

print("_"*50)
# loop with indexing
for i in range(0, len(str10), 1):
    print(i, str10[i])

print("_"*50)
for i, char in enumerate(str10):
    print(i, char)
