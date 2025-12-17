# Python code to generate dictionary output from given string.

str1 = "Hello we Are Learning Python"
# expected output1 = {'H': 'Hello', 'w': 'we', 'A': 'Are', 'L': 'Learning', 'P': 'Python'}

# empty dict variable
output1 = {}
# split to get list of words
word_list = str1.split(" ") # ['Hello', 'we', 'Are', 'Learning', 'Python']
print(word_list)

for word in word_list: # Hello
    f_char = word[0]  # H
    output1[f_char] = word  # H: Hello
    print(output1)

print("output1 :", output1)

print("#"*50)
#######################################################################
#Home Work Python code to generate dictionary output from given string.

str2 = "Hello we Are Learning Python"
# expected output1 = {'Ho': 'Hello', 'we': 'we', 'Ae': 'Are', 'Lg': 'Learning', 'Pn': 'Python'}

word_list=str2.split(" ") # ['Hello', 'we', 'Are', 'Learning', 'Python']
print(word_list)
output2 = {}
for word in word_list: # Hello
    first_char= word[0]
    last_char= word[-1]# Ho
    output2[first_char+last_char] = word # Ho: Hello
    print(output2)

print("output2 :", output2)

print("_" * 50)
#######################
# write a python program to create a dictionary from given string.
str1 = "We are learning Python"
# output = {"W": We, "a": "are", "l": "learning", "P": "Python"}

word_list = str1.split(" ")
print(word_list)  # ['We', 'are', 'learning', 'Python']
result = {}
for word in word_list:  # We, are, learning
    first_char = word[0]  # W, a, l
    result[first_char] = word
    print(result)

print("Result :", result)
# Result : {'W': 'We', 'a': 'are', 'l': 'learning', 'P': 'Python'}