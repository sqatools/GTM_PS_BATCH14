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
print("Longest word: ", max(word_list, key=len))
print("Smallest word: ", min(word_list, key=len))

print("-" * 100)
# 8). Print most simultaneously repeated characters in the input string.
str9 = "theee data"
max_repeat_char = ""
max_repeat_count = 0
temp = 1
for i in range(len(str9) - 1):
    if str9[i] == str9[i + 1]:
        temp = temp + 1
        if temp > max_repeat_count:
            max_repeat_count = temp
            max_repeat_char = str9[i]
        else:
            temp = 1
print("Maximum character: ", max_repeat_char, "\nMaximum count: ", max_repeat_count)
