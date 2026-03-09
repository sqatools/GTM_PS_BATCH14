# 1> Write a Python program to get a string made of the first and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string

str1 = "Hello Python"
if len(str1) < 2:
    print("The First program o/p :", True)
else:
    print("The First program o/p :", str1[0:2] + str1[-2:])

print("-" * 100)
# 2> Python string program that takes a list of strings and returns the length of the longest string.
str2 = ["Hi", "Hello", "Programming", "is"]
count = 0
for word in str2:
    a = len(word)
    if a > count:
        count = a
print("The Longest string: ", count)

print("-" * 100)
# 3> Python string program to get a string made of 4 copies of the last two characters of a
# specified string (length must be at least 2).
str3 = "Python"
str4 = str3[-2:] * 4
print("Get a string made of 4 copies:", str4)

print("-" * 100)
# 4> Python string program to reverse a string if it’s length is a multiple of 4.
str5 = "Hello User 1"
print("Length is: ", len(str5))
if len(str5) % 4 == 0:
    print("Reverse String is :", str5[::-1])
else:
    print("The string length is not multiple of 4")

print("-" * 100)
# 5> Python string program to count occurrences of a substring in a string
str6 = "Hello User, This is the user specific event"
print("count occurrences of a substring: ", str6.count("User"))

print("-" * 100)
# 6> Python string program to test whether a passed letter is a vowel or consonant
str7 = "Java is program"
for ch in str7:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        print(f"The {ch} which in passed is vowel")
    else:
        print(f"The {ch} which in passed is constant")

print("-" * 100)
# 7> Find the longest and smallest word in the input string.
str8 = "The python program is fun"
word_list = str8.split(" ")
print("Longest word: ", max(word_list, key = len))
print("Smallest word: ", min(word_list, key = len))

print("-" * 100)
# 8). Print most simultaneously repeated characters in the input string.
str9 = "theeeeeeee data, userrrrrrrrrrrr"
print("split output:", str9.split(" "))
max_repeat_char = ""
max_repeat_count = 0
temp = 1
for i in range(len(str9) - 1):
    if str9[i] == str9[i + 1]:
        temp += 1
        if temp > max_repeat_count:
            max_repeat_count = temp
            max_repeat_char = str9[i]
    else:
        temp = 1
print("Maximum character: ", max_repeat_char, "\nMaximum count: ", max_repeat_count)

print("-"*100)
s = "we-learning-Python"
print(s.split("-", maxsplit=1))
print(s.rsplit("-", maxsplit=1))

print("-"*100)
# 9> Write a Python program to calculate the length of a string with loop logic.
str10 = "Python Program"
count = 0
for val in str10:
    count = count+1
print("Length of the string using loop logic: ", count)
print("Length of the string using len(): ", len(str10))

print("-"*100)
# 10). Write a Python program to replace the second occurrence of any char with the special character $.
# Input = “Programming”
# Output = “Prog$am$in$”
str11 = "Programming"
output=""
for char in str11:
    if char in output:
        output = output+"$"
    else:
        output = output+char

print("output:", output)

print("-"*100)
# 11). Write a python program to get to swap the last character of a given string.
#Output = “lqaTooS”
input = "SqaTool"
output = "l"+input[1:-1] + "S"
print(output)

print("-"*100)
# 12). Write a python program to exchange the first and last character of each word from the given string.
# Input = “Its Online Learning”
# Output = “stI enlino gearninL”

str12 = "Its Online Learning"
output = ""
output = "s"+str12[1:-17] + "I" + " " \
         + "e"+str12[5:-10] + "O" + " " \
         + "g"+str12[12:-1] + "L" + " "
print(output)

#OR
str12 = "Its Online Learning"
word_list = str12.split()
for word in word_list:
    output = word[-1]+word[1:-1]+word[0]
    index = word_list.index(word)
    word_list[index] =output

print(" ".join(word_list))

print("-"*100)
# 13). Write a python to count vowels from each word in the given string show as dictionary output.
# Input = “We are Learning Python Codding”
# output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}

str13 = "We are Learning Python Codding"
word_lst = str13.split(" ")
vowels = "aeiou"
output = dict()

for word in word_lst:
    count = 0
    for char in word:
        if char in vowels:
            count +=1
        output[word]= count

print(output)

print("-"*100)
# 14). Write a python to repeat vowels 3 times and consonants 2 times.
# Input = “Sqa Tools Learning”
# Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”
input = "Sqa Tools Learning"
output =""
vowels = ["a","e","i","o","u",
          "A","E","I","O","U"]
for char in input:
    if char in vowels:
        output = output + char*2
    else:
        output = output + char*3

print(output)

print("-"*100)
# 15). Write a python program to re-arrange the string.
str15 = "Cricket Plays Virat"
word_lst = str15.split(" ")
word_lst.reverse()
print("Final string: ", " ".join(word_lst))

print("-"*100)
# 16). Write a python program to get all the digits from the given string.
# Input = “””
# Sinak’s 1112 aim is to 1773 create a new generation of people who
# understand 444 that an organization’s 5324 success or failure is
# based on 555 leadership excellence and not managerial
# acumen
# “””
# Output = [1112, 5324, 1773, 5324, 555]
str16 = "Sinak’s 1112 aim is to 1773 create a new generation of people who understand 444 that an organization’s 5324 success or failure is based on 555 leadership excellence and not managerial acumen"
word_lt = str16.split(" ")
list = []
for word in word_lt:
    if word.isdigit():
        list.append(word)
    else:
        continue
print(list)

print("-"*100)
# 17). Write a python program to replace the words “Java” with “Python” in the given string.
# Input = “JAVA is the Best Programming Language in the Market”
# Output = “Python is the Best Programming Language in the Market”
str17 = "JAVA is the Best Programming Language in the Market"
output = str17.replace("JAVA", "Python")
print("Exchange words:", output)

print("-"*100)
# 18). Write a Python program to get all the palindrome words from the string.
# Input = “Python efe language aakaa hellolleh”
# output = [“efe”, “aakaa”, “hellolleh”]
str18 = "Python efe language aakaa hellolleh"
word_list = str18.split(" ")
list = []
for word in word_list:
    if word == word[::-1]:
        list.append(word)
print(list)

print("-"*100)
# 19). Write a Python program to create a string with a given list of words.
# Input = [“There”, “are”, “Many”, “Programming”, “Language”]
# Output = There are many programming languages.
str19 = ["There", "are", "Many", "Programming", "Language"]
output = " ".join(str19)
print(output)

print("-"*100)
# 20). Write a Python program to remove duplicate words from the string.
# Input = “john jany sabi row john sabi”
# output = “john jany sabi row”
str20 = "John jany sabi row john sabi"
word_list = str20.lower().split(" ")
list2 = []
for val in word_list:
    if val not in list2:
        list2.append(val)


print(" ".join(list2))

print("-"*100)
#21). Write a Python to remove unwanted characters from the given string.
# Input = “Prog^ra*m#ming”
# Output = “Programming”

# Input = “Py(th)#@&on Pro$*#gram”
# Output = “PythonProgram”
str21 = "Prog^ra*m#ming"
str22 = "Py(th)#@&on Pro$*#gram"
output1 = ""
output2 = ""
for char in str21:
    if char.isalnum():
        output1 += char
print(output1)

# 22). Write a Python program to find the longest capital letter word from the string.
# Input = “Learning PYTHON programming is FUN”
# Output = “PYTHON”

str23 = "Learning PYTHON programming is FUN"
word_list = str23.split(" ")
cap_word = ""
for word in word_list:
    if word.isupper() and len(word) > len(cap_word):
        cap_word = word
print("Longest capital letter word: ", cap_word)

print("-"*100)

# 23). Write a Python program to get common words from strings.
# Input String1 = “Very Good Morning, How are You”
# Input String2 = “You are a Good student, keep it up”
# Output = “You Good are”

str24_1 = "Very Good Morning, How are You"
str24_2 = "You are a Good student, keep it up"  
word_list1 = str24_1.replace(",", "").split(" ")
word_list2 = str24_2.replace(",", "").split(" ")    
common_words = []
for word in word_list1:
    if word in word_list2:
        common_words.append(word)   
print("Common words: ", " ".join(common_words))
print("-"*100)

# 24). Write a Python program to find the smallest and largest word in a given string.
# Input = “Learning is a part of life and we strive”
# Output = “a”, “Learning”

str25_1 = "Learning is a part of life and we strive"
smallest = str25_1.split(" ")[0]
longest = ""
word_list1 = str25_1.split(" ")
for word in word_list1:
    if len(word) > len(longest):
       longest = word
    elif len(word) <len(smallest):
        smallest = word
print(longest)
print(smallest)
# using min and max

# 25). Check whether the given string is a palindrome (similar) or not.
# Input= sqatoolssqatools
# Output= Given string is not a palindrome

input = "sqatoolssqatools"
output = input[::-1]
print(output)
if input == output:
    print("Given string is a palindrome")
else:
    print("Given string is not a palindrome")

# 26). Write a program using python to reverse the words in a string.
# Input= sqatools python
# Output= slootaqs

str26 = "sqatools python"
word_list26 = str26.split(" ")
word1 = word_list26[0]
print("The output is:", word1[::-1])

# reverse the word in string
print(" ".join(word_list26[::-1]))

# 27). Write a program to calculate the length of a string.
# Input= “python”
# Output = 6
str_27 = "python"
print("The length is:", len(str_27))

# 28). Write a program to calculate the frequency of each character in a string.
# Input = “sqatools”
# Output = {‘s’:2, ‘q’:1, ‘a’: 1, ‘t’:1,‘o’:2, ‘l’:1, ‘s’:1}

str_28 = "sqatools"
dictionary = dict()
for char in str_28:
    dictionary[char] = str_28.count(char)
print(dictionary)

#29). Write a program to combine two strings into one.
"""Input: 
A = ’abc’
B = ’def’
Output = abcdef"""
a = 'abc'
b = 'def'
print("Output is:", a+b)

#30). Write a program to print characters at even places in a string.
# Input = ‘sqatools’
# Output = saol

str_30 = "sqatools"
for i in range(len(str_30)):
    if i%2 == 0:
        print(str_30[i], end=" ")

# 31). Write a program to check if a string has a number or not.
#Input = ‘python1’
#Output = ‘Given string have a number’
#Input string
string = "abc"
count = 0

for char in string:
    if char.isnumeric():
        count += 1

#Checking for numbers
if count > 0:
    print("\nGiven string have a number")
else:
    print("\nGiven string does not have a number")

# 32). Write a python program to count the number of vowels in a string.
# Input= ‘I am learning python’
# Output= 6
str_32 = "I am learning python"
vowels = "aeiou"
count = 0
for char in str_32:
    if char.lower() in vowels:
        count += 1
print("Vowels are:", count)

# 33). Write a python program to count the number of consonants in a string.
# Input= ‘sqltools’
# Output= 6
str_33 = "sqatools"
vowels = "aeiou"
count = 0
for char in str_33:
    if char.lower() not in vowels:
        count += 1
print("Constants are:", count)

# 34). Write a program to print characters at odd places in a string.
# Input = ‘abcdefg’
# Output = ‘bdf’
str_34 = "abcdefg"
for i in range(len(str_34)):
    if i%2 != 0:
        print(str_34[i], end="")

# 35). Write a program to remove all duplicate characters from a given string in python.
# Input = ‘sqatools’
# Output = ‘sqatol’
str_35 = "sqatools"
output =""
for char in str_35:
    if char not in output:
        output = output+char
print("\nremove duplicates:", output)

# "OR"
from collections import OrderedDict
print("\nremove duplicates:","".join(OrderedDict.fromkeys(str_35)))

# 36). Write a program to check if a string has a special character or not
# Input = ‘python$$#sqatools’
# Output =  ‘Given string has special characters
str_36 = "python$$#sqatools"
s ='[@_!#$%^&*()<>?/\|}{~:]'
count = 0

for char in str_36:
    if char in s:
        count += 1
        
if count > 0:
    print("Given string has special characters")
else:
    print("Given string not contains special characters")

# 37). Write a program to exchange the first and last letters of the string
# Input = We are learning python
# Output = ne are learning pythoW
str_37 = "We are learning python"
output = str_37[-1] + str_37[1:-1]+ str_37[0]
print("Exchane first and last letters:", output)


# 38). Write a program to convert all the characters in a string to Upper Case.
# Input = ‘I live in pune’
# Output = ‘I LIVE IN PUNE’
str_38 = "I live in pune"
print("The uppercase letter:", str_38.upper())

# 39). Write a program to remove a new line from a string using python.
# Input = ‘objectorientedprogramming\n’
# Output = ‘Objectorientedprogramming’
str_39 = "objectorientedprogramming\n"
print(str_39)
print("remove a new line: ", str_39.rstrip())

# 40). Write a python program to split and join a string
"""Input =‘Hello world’
Output = [‘Hello’, ‘world’]
                 Hello-world"""
str_40 = "Hello world"
a = str_40.split(" ")
print(a)
print("-".join(a))

# 41). Write a program to print floating numbers up to 3 decimal places and convert it to string.
# Input = 2.14652
# Output= 2.146

a = 2.14652
result = ""
out = round(a,3)
result = result + str(out)
print(result)

#42). Write a program to convert numeric words to numbers.
# Input = ‘five four three two one’
# Output = 54321
str_42 = "five four three two one"
str_output = ""
words = str_42.split(" ")
for word in words:
    if word == "one":
        str_output += "1" 
    if word == "two":
        str_output += "2"
    if word == "three":
        str_output += "3" 
    if word == "four":
        str_output += "4" 
    if word == "five":
        str_output += "5" 
    if word == "six":
        str_output += "6" 
    if word == "seven":
        str_output += "7"
    if word == "eight":
        str_output += "8" 
    if word == "nine":
        str_output += "9"
    if word == "zero":
        str_output += "0" 
print(str_output)

# 43). Write a python program to find the location of a word in a string
#Input Word = ‘problems’
#Input string = ‘ I am solving problems based on strings’
#Output = 4
strloc = "I am solving problems based on strings"
str_word = "problems"
words = strloc.split(" ")
output = words.index(str_word)
print("The index of Problem is: ", output)

# 44). Write a program to count occurrences of a word in a string.
"""
Word = ‘food’
Input str = ‘ I want to eat fast food’
Occurrences output= 1

Word = ‘are’
Input str = “We are learning Python, wow are you”
Occurrences output = 2 """
input1 = "I want to eat fast food"
words1 = input1.split(" ")
print("Count of Food:", words1.count("food"))

input2 = "We are learning Python, wow are you"
words2 = input2.split(" ")
print("Count of are:", words2.count("are"))

# 45). Write a python program to find the least frequent character in a string.
#Input =  ‘abcdabdggfhf’
#Output = ‘c’
str_45 = "abcdabdggfhf"
dict = {}
for char in str_45:
    if char in dict:
        dict[char] = dict[char] + 1
    else:
        dict[char] = 1
    result = min(dict, key=dict.get)
print("The lease frequent char is:", result)

# 46). Find the words greater than the given length.
#Ex length = 3
#Input = ‘We are learning python’
#Output – ‘learning python’

str_46 = "We are learning python"
min_len = 3
output = ""
words3 = str_46.split(" ")
for word in words3:
    if len(word) > 3:
        output = output + word + " "
    print(output)

#47). Write a program to get the first 4 characters of a string.
#Input = ‘Sqatools’
#Output = ‘sqat’
str_47 = "Sqatools"
print("The first four characters are: ", str_47[0:4])

#48). Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# Input = ‘Sqatools’
# Output = ‘Sqls’ 
str_48 = "Sqatools"
print(str_48[:2] + str_48[-2:])

#49). Write a python program to print the mirror image of the string.
# Input = ‘Python’
# Output = ‘nohtyp 
str_49 = "Python"
print("Mirror or reverseo of string:", str_49[::-1])

#50). Write a python program to split strings on vowels
# Input = ‘qwerty’
# Output = ‘qw rty’
str_50 = "qwerty"
vowels ="aeiou"
output =""
for ch in str_50:
    if ch not in vowels:
        output = output+ch
    else:
        output = output + " "
print(output)

import re
str_50 = "qwerty"
output = re.split("a|e|i|o|u", str_50)
print(" ".join(output))

# 51). Write a python program to replace multiple words with certain words.
"""Input = “I’m learning python at Sqatools”
Replace python with SQA  and sqatools with TOOLS 
Output = “I’m learning SQA at TOOLS “ """
str_51 = "I'm learning python at Sqatools"
output = str_51.replace("python", "SQA")
output1 = output.replace("Sqatools", "TOOLS")
print("The replaced words: ", output1)

#Input string
string = "I’m learning python at Sqatools"
List = string.split(" ")

for i in range(len(List)):
    if List[i] == "python":
        List[i] = "SQA"
    elif List[i] == "Sqatools":
        List[i] = "TOOLS"

#Printing output
print(" ".join(List))

# 52). Write a python program to replace different characters in the string at once.
"""Input = ‘Sqatool python’
Replace a with 1,
Replace t with 2,
Replace o with 3
Output = ‘sq1233l py2h3n” """
string = "Sqatool python"
output = string.replace("a", "1")
output1 = output.replace("t", "2")
output2 = output1.replace("o", "3")

print(output2)

#######################################
string = "Sqatool python"
new_str = ""
for ch in string:
    if ch == "a":
        new_str += "1"
    elif ch == "t":
        new_str += "2"
    elif ch == "o":
        new_str += "3"   
    else:
        new_str += ch 

#Printing output
print(new_str)

# 53). Write a python program to remove empty spaces from a list of strings.
#Input = [‘Python’, ‘ ‘, ‘ ‘, ‘sqatools’]
#Output = [‘Python’, ‘sqatools’] 

str_53 = ["Python", " ", " ", "sqatools"]
list = []
for word in str_53:
    if word != " ":
        list.append(word)
print(list)

# 54).  Write a python program to remove punctuations from a string
#Input = ‘Sqatools : is best, for python’
#Output = ‘Sqatools is best for python’
str_54 = "Sqatools : is best, for python"
result_54 = ""
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for ch in str_54:
    if ch not in punc:
        result_54 += ch
print(result_54)

###########################################
import string

str_54 = "Sqatools : is best, for python"
result = ""

for ch in str_54:
    if ch not in string.punctuation:
        result += ch

result1 = result.split(" ")
print(" ".join(result1))


# 55).  Write a python program to find duplicate characters in a string
#Input = “hello world”
#Output = ‘lo’
str_55 = "hello world"
result_55 = []
for ch in str_55:
    if str_55.count(ch) > 1:
       result_55.append(ch)
print(set(result_55))

# 56).  Write a python program to check whether the string is a subset of another string or not
"""Input str1 = “iamlearningpythonatsqatools”
str = ‘pystlmi’
Output = True """
string1 = "iamlearningpythonatsqatools"
string2 = "pystlmi"
string3 = set(string1)
print(string3)
count = 0
for ch in string3:
    if ch in string2:
        count += 1
if count == len(string2):
    print("True")
else:
    print("False")

# 57). Write a python program to sort a string
#Input = ‘xyabkmp’
#Output = ‘abkmpxy’
input = "xyabkmp"
print("The sorting is:", "".join(sorted(input)))

#58). Write a python program to generate a random binary string of a given length.
#Input = 8
#Output = 10001001
import random
input = 8
output = ""
for i in range(9):
    val = str(random.randint(0,1))
    output += val
print(output)

# 59). Write a python program to check if the substring is present in the string or not
# Input string= ‘I live in Pune’
# Substring= ‘I live ‘
# Output = ‘Yes

str_59 = "I live in Pune"
substr = "I live"
word_list1 = str_59.split(" ")
word_list2 = substr.split(" ")
count = 0
for word in word_list1:
    if word in word_list2:
        count = count + 1

if count == len(word_list2):
    print("true")
else:
    print("false")

# 60). Write a program to find all substring frequencies in a string.
#Input str1 = “abab” 
#Output = {‘a’: 2, ‘ab’: 2, ‘aba’: 1,‘abab’: 1, ‘b’: 2, ‘ba’: 1, ‘bab’: 1}  
str1 = "abab"

substrings = []
freq = {}

for i in range(len(str1)):
    for j in range(i+1, len(str1)+1):

        sub = str1[i:j]
        substrings.append(sub)

        if sub in freq:
            freq[sub] += 1
        else:
            freq[sub] = 1

print(freq)

# 61). Write a python program to print the index of the character in a string.
#Input = ‘Sqatools’
#Output = ‘The index of q is 1’

input = "Sqatools"
print("The index of letter is 1:", input.index('o'))

# 62). Write a program to strip spaces from a string.
#Input = ‘    sqaltoolspythonfun     ‘ 
#Output = ‘ sqaltoolspythonfun’
input = "    sqaltoolspythonfun     "
print(input.strip())

# 63). Write a program to check whether a string contains all letters of the alphabet or not.
# Input = ‘abcdgjksoug’
# Output = False
#Importing string
import string
alphabet = set(string.ascii_lowercase)

#Input string
string = "abcdgjksoug"

#Printing output
print(set(string.lower()) >= alphabet)

# 64). Write a python program to convert a string into a list of words.
#Input = ‘learning python is fun’
#Output = [learning, python, is, fun] 
input = "learning python is fun"
print(input.split(" "))

# 65). Write a python program to swap commas and dots in a string.
# Input = sqa,tools.python
# Output = sqa.tools,python
input = "sqa,tools.python"
print(input.replace(",", "#"))
print(input.replace(".", ","))
print(input.replace("#", "."))

input1 = "sqa,tools.python"
table = input1.maketrans(",.", ".,")
result = input1.translate(table)
print(result)

# 66). Write a python program to count and display the vowels in a string
#Input = ‘welcome to Sqatools’
#Output = 70
str66 = "welcome to a ESqatools"
vowels = "aeiou"
count = 0
for ch in str66:
    if ch.lower() in vowels:
        count = count + 1
print(count)

# 67). Write a Python program to split a string on the last occurrence of the delimiter. 
#Input = ‘l,e,a,r,n,I,n,g,p,y,t,h,o,n’
#Output = [‘l,e,a,r,n,I,n,g,p,y,t,h,o ‘ ,’n’]
str67 = "l,e,a,r,n,I,n,g,p,y,t,h,o,n" 
print(str67.rsplit(",", 1))

#68). Write a Python program to find the first repeated word in a given string. 
#Input = ‘ab bc ca ab bd’
#Output = ‘ab’
str68 = "ab bc ca ab bd"
output = []
word_split = str68.split(" ")
print(word_split)
for word in word_split:
    if word not in output:
        print(word)
        break
    else:
        output.append(word)
    
# 69). Write a program to find the second most repeated word in a given string using python.
#Input = ‘ab bc ac ab bd ac nk hj ac’
#Output = (‘ab’, 2)
#Input string
string = "ab bc ac ab bd ac nk hj ac"
dictionary = {}

for char in string.split(" "):
    if char != " ":
        dictionary[char] = string.count(char)

counts_ = sorted(dictionary.items(), key=lambda val: val[1])
#Printing output
print(counts_[-2])

# 70). Write a Python program to remove spaces from a given string.
#Input = ‘python at sqatools’
#Output = ‘pythonatsqatools’
str70 = "python at sqatools"
print(str70.replace(" ", ""))

# 71). Write a Python program to capitalize the first and last letters of each word of a given string.
#Input = ‘this is my first program’
#Output = ‘ThiS IS MY FirsT PrograM’
str_71 = "this is my first program"
word = str_71.split(" ")
for ch in word:
    print(ch[0].upper() + ch[1:-1] + ch[-1].upper(), end= " ")

# 72). Write a Python program to calculate the sum of digits of a given string.
#Input = ’12sqatools78′
#Output = 18
str72 = "12sqatools78"
total = 0
for ch in str72:
    if ch.isnumeric():
        total = total + int(ch)
print("\n", total)

# 73). Write a Python program to remove zeros from an IP address. 
#Input = 289.03.02.054
#Output = 289.3.2.54
#Importing re
import re

#Input string
str1 = "289.03.02.054"

string = re.sub('\.[0]*', '.', str1)

#Printing output
print(string)

#74). Write a program to find the maximum length of consecutive 0’s in a given binary string using python.
Input = "10001100000111"
result = Input.split("1")
result1 = max(result, key = len)
print(len(result1))

Input = "10320000041000001110000"

count = 0
max_count = 0

for ch in Input:
    if ch == "0":
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0

print(max_count)

# 75). Write a program to remove all consecutive duplicates of a given string using python.
#Input = ‘xxxxyy’
#Output = ‘xy’

s = "xxxxyy"
result = s[0]

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        result += s[i]

print(result)

#Input string
str1= "xxxxyy"
list1 = []

#Importing group
from itertools import groupby

for (key,group) in groupby(str1):
    list1.append(key)

#Printing output
print("".join(list1))

# 76). Write a program to create strings from a given string. Create a string that consists of multi-time occurring characters in the said string using python.
#Input = “aabbcceffgh”
#Output = ‘abcf’
str76 = "aabbcceffggghiiijj"
result = ""
for ch in str76:
    if str76.count(ch)>1 and ch not in result:
        result += ch
print(result)


#Input string
str1 = "aabbcceffgh"

#Importing counter
from collections import Counter
str_char = Counter(str1)

part1 = [ key for (key,count) in str_char.items() if count>1]

#printing output
print("Occurring more than once: ", "".join(part1))

# 77). Write a Python program to create a string from two given strings combining uncommon characters of the said strings.  
"""
Input string :
s1 = ‘abcdefg’
s2 = ‘xyzabcd’
Output string : ‘efgxyz’"""
s1 = "abcdefg"
s2 = "xyzabcd"
output = ""
for ch in s1:
    if ch not in s2:
        output = output+ch
for ch in s2:
    if ch not in s1:
        output = output+ch    

print(output)

# 78). Write a Python code to remove all characters except the given character in a string. 
"""Input = “Sqatools python”
Remove all characters except S
Output = ‘S’"""
str78 = "Sqatools python"
output = "" 
for ch in str78:
    if ch == "S":
        output = output + ch
print(output)

# 79). Write a program to count all the Uppercase, Lowercase, special character and numeric values in a given string using python.
"""Input = ‘@SqaTools.lin’
Output:
Special characters: 1
Uppercase characters: 2
Lowercase characters: 8 """
str79 = "@SqaTools.lin"
upper = 0
lower = 0 
digit = 0
special = 0
for ch in str79:
    if ch.islower():
        lower = lower + 1
    elif ch.isupper():
        upper = upper + 1
    elif ch.isdigit():
        digit = digit + 1
    else:
        special = special+1
print("Special characters:", special)
print("Uppercase characters:", upper)
print("Lowercase characters:", lower)

#80). Write a Python program to count a number of non-empty substrings of a given string.
#Input a string = ‘sqatools12’
#Number of substrings = 55
str80 = "sqatools12"
n = len(str80)
count = n * (n+1) //2
print(count)

# 81). Write a program to remove unwanted characters from a given string using python.
#Input = ‘sqa****too^^{ls’
#Output = ‘Sqatools’
import string
str81 = "sqa****too^^{ls"
output = ""
for ch in str81:
    if ch not in string.punctuation:
        output = output + ch

print(output)

# 82). Write a program to find the string similarity between two given strings using python.
"""Input : 
Str1 = ‘Learning is fun in Sqatools’
Str2 = ‘Sqatools Online Learning Platform’

Output :
Similarity : 0.4"""
import difflib
str1 = "Learning is fun in Sqatools"
str2 = "Sqatools Online Learning Platform"
result = difflib.SequenceMatcher(a=str1.lower(), b=str2.lower())
print(result.ratio())

# 83). Write a program to extract numbers from a given string using python.
#Input = ‘python 456 self learning 89’
#Output = [456, 89]
str83 = "python 456 self learning 89"
list = str83.split(" ")
list2 = []
for word in list:
    if word.isdigit():
        list2.append(int(word))
print(list2)

# 84). Write a program to split a given multiline string into a list of lines using python.
"""Input =”’This string Contains
Multiple
Lines”’
Output = [‘This string Contains’, ‘Multiple’, ‘Lines’] """

str84 = "This string Contains\nMultiple\nLines"
print("Multiline split:", str84.split("\n"))

# 85). Write a program to add two strings as they are numbers using python.
"""Input :
a=’3′, b=’7′
Output  = ’10’ """

a = "3"
b = "7"
a1 = int(a)
b1 = int(b)
print(a1,b1)
c = a1+b1
print(c)

# 86). Write a program to extract name from a given email address using python.
"""Input = ‘student1@gmail.com’
Output = ‘student’ """

email = "student1@gmail.com"
name = email.split("@")[0]
result = ""
print(name)
for word in name:
    if word.isalpha():
        result = result + word
print(result)

# 87). Write a  program that counts the number of leap years within the range of years using python. The range of years should be accepted as a string. 

#(“1981-2001)  =  Total leap year 5
year = "1981-2001"
y = year.split("-")
year1 = int(y[0])
year2 = int(y[1])

count = 0

for year in range(year1, year2 + 1):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        count += 1

print("Total leap years:", str(count))

# 88). Write a program to insert space before every capital letter appears in a given word using python. 
"""Input = ‘SqaTools pyThon’
Output = ‘ Sqa Tools py Thon’ """

str88 = "SqaTools pyThon"
output = ""
for ch in str88:
    if ch.isupper():
        output = output + " " + ch
    else:
        output = output + ch
print(output)

# 89). Write a program to uppercase half string using python.
#Input = ‘banana’
#Output = ‘banANA’
str89 = "banana"
output =""
length = len(str89)//2
for i in range(0, length):
    output = output + str89[i]
for i in range(length, len(str89)):
    output = output + str89[i].upper()
print("solution1", output)
output = str89[:len(str89)//2] + str89[len(str89)//2:].upper()
print("solution2", output)
output = str89[:3]+str89[3:-3]+str89[3:].upper()
print("solution3", output)

# 90). Write a program to split and join a string using “-“.
#Input = ‘Sqatools is best’
#Output = ‘Sqatools-is-best’
str90 = "Sqatools is best"
print("-".join(str90.split(" ")))

# 91). Write a python program to find permutations of a given string using in built function.
#Input  = ‘CDE’
#Output = [‘CDE’, ‘CED’ ‘EDC’, ‘ECD’, ‘DCE’, ‘DEC’]
from itertools import permutations

str1 = "CDE"
list_data = []
for p in permutations(str1):
    list_data.append("".join(p))
print(list_data)

# 92). Write a program to avoid spaces in string and get the total length
#Input = ‘sqatools is best for learning python’
#Output = 31
str92 = "sqatools is best for learning python"
result = sum(not char.isspace() for char in str92)
print(result)
output = str92.replace(" ", "")
print(len(output))

# 93). Write a program to accept a string that contains only vowels
"""Input = ‘python’
Output- ‘not accepted’

Input = ‘aaieou’
Output = ‘accepted’ """
str93 = "AaTesiuu"
vowels = "aeiou"
count = 0
for ch in str93:
    if ch.lower() in vowels:
        count = count + 1
if count == len(str93):
    print("Accepted")
else:
    print("Not Accepted")

# 94). Write a program to remove the kth element from the string
#K=2
#Input = ‘sqatools’
#Output = ‘sqtools’
str94 = "sqatools"
k = 2
print(str94.index('a'))
print(str94[:2]+ str94[3:])
print(str94[:k]+ str94[k+1:])

# 95). Write a program to check if a given string is binary or not.
"""Hint: Binary numbers only contain 0 or 1.

Input = ‘01011100’
Output = yes

Input = ‘sqatools 100’
Output = ‘No’ """

in1  = "01011100"
count = 0
for ch in in1:
    if ch == "0" or ch == "1":
        count += 1
if count == len(in1):
    print("Yes")
else:
    print("No")

#96). Write a program to add ‘ing’ at the end of the string using python.
#Input = ‘xyz’
#Output = ‘xyzing’

str96  = "xyz"
b = "ing"
print(str96+b)
print(str96 + "ing")

# 97). Write a program to add ly at the end of the string if the given string ends with ing.
#Input = ‘winning’
#Output = ‘winningly’

str97 = "winning"
if str97.endswith("ing"):
    print(str97+ "ly")
else:
    print(str97)

#98). Write a program to reverse words in a string using python.
#Input = ‘string problems’
#Output = ‘problems string’
str98 = "string problems"
word_list = str98.split(" ")
list = ""
print(" ".join(word_list[::-1]))

# 99). Write a program to print the index of each character in a string.
"""Input =  ‘sqatools’
Output :
Index of s is 0
Index of q is 1
Index of a is 2
Index of t is 3
Index of o is 4
Index of o is 5
Index of l is 6
Index of s is 7 """
str99 = "sqatools"
for ch in str99:
    print("Index of", ch, "is:", str99.index(ch))

# 100). Write a program to find the first repeated character in a string and its index.
#Input = ‘sqatools’
#Output = (s,0)
str100 = "sqatools"
for i in range(len(str100)):
        for j in range(i+1, len(str100)):
            if str100[i] == str100[j]:
                print(f"({str100[i]}, {str100.index(str100[i])})")
                break

# 101). Write a program to swap cases of a given string using python.
#Input = ‘Learning Python’
#Output = ‘lEARNING pYTHON’
str101 = "Learning Python"
print("swapcase result:", str101.swapcase())

# 102). Write a program to remove repeated characters in a string and replace it with a single letter using python.
#Input = ‘aabbccdd’
#Output = ‘cabd’
str102 = "aabbccdd"
lst = set(str102)
print("".join(lst))

# 103). Write a program to print a string 3 times using python.
#Input = ‘sqatools’
#Output = ‘sqatoolssqatoolssqatools’
str103 = "sqatools"
print("Repeat string:", str103*3)

#104). Write a program to print each character on a new line using python.
"""Input = ‘python’
Output:
p
y
t
h
o
n """
str104 = "python"
for ch in str104:
    print(ch, end= "\n")

# 105). Write a program to get all the email id’s from given string using python.
#Input str = “”” We have some employee whos john@gmail.com email id’s are randomly distributed jay@lic.com we want to get hari@facebook.com all the email mery@hotmail.com id’s from this given string.”””
#Output = [‘john@gmail.com’, ‘ jay@lic.com’, ‘hari@facebook.com’, ‘mery@hotmail.com’ ]
str105 = "We have some employee whos john@gmail.com email id’s are randomly distributed jay@lic.com we want to get hari@facebook.com all the email mery@hotmail.com id’s from this given string."
word_list = str105.split(" ")
print(word_list)
list1 =[]
for word in word_list:
    if word.endswith(".com"):
        list1.append(word)
print(list1)

# 106). Write a program to get a list of all the mobile numbers from the given string using python.
#Input str = “”” We have 2233 some employee 8988858683 whos 3455 mobile numbers are randomly distributed 2312245566 we want 453452 to get 4532892234 all the mobile numbers 9999234355  from this given string.”””
# Output = [‘8988858683’, ‘2312245566’, ‘4532892234’, ‘9999234355’]
str106 = "We have 2233 some employee 8988858683 whos 3455 mobile numbers are randomly distributed 2312245566 we want 453452 to get 4532892234 all the mobile numbers 9999234355  from this given string."
word_list = str106.split(" ")
list1 = []
for word in word_list:
    if word.isdigit() and len(word)>=10:
        list1.append(word)
print(list1)
