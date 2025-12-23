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

