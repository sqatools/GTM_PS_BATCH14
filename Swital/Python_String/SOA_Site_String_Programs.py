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