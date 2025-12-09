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

word_list = str5.split(" ")
print(word_list)
result= " "

for word in word_list:
    if len(word) % 2 ==0:
        result= result + word.lower()+ " "
    else:
        result= result +word.upper() + " "

print(result)


