#Q1 :  write a python program to count total vowels from given string.
str1 = "Hello we are LeArning PythOn"
vowels = "aeiou"
count = 0
for char in str1:
    if char in vowels:
        count += 1
    else:
        continue
print(count)

#q2 :  write a python program remove duplicate character from given string and generate output.
print("#"*50)
str2 = "Hello we are LeArning PythOn"
output = ""
for char in str2:
    if char.lower() not in output:
        output = output+char
    else:
        continue
print(output)



#Q5 write a python program to convert odd length word in upper case and even length word in lower case.
print("#"*50)
# output = "INDIA is best COUNTRY in THE WORLD"
str_a = "India iS BesT country in the world"
str_output = ""
str_b = str_a.split(" ")
for word in str_b:
    if len(word)%2 != 0:
        output = word.upper()
    else:
        output = word.lower()

    str_output = str_output+output+ " "

print(str_output)


print("#"*50)
str6 = "Everything is possible with hardwork"
word_split = str6.split(" ")
longest = ""
second_longest=""
word_len = 0
for word in word_split:
    if len(word)>word_len:
        word_len = len(word)
        second_longest = longest
        longest = word
    elif len(word)<word_len and len(word)>len(second_longest):
        second_longest = word
print(second_longest)

print("#"*50)
str8 = "Motivation inspires dedication and give us strength"