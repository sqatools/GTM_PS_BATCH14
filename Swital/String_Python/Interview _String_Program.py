#Q5 write a python program to convert odd length word in upper case and even length word in lower case.
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
