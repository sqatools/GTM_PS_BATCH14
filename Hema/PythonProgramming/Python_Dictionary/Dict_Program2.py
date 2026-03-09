str2 = "Hello we Are Learning Python"
# expected output1 = {'Ho': 'Hello', 'we': 'we', 'Ae': 'Are', 'Lg': 'Learning', 'Pn': 'Python'}
output_2= {}
word_list = str2.split(" ")
print(word_list)
for word in word_list:
    f_char = word[0]
    f_char2 = word[-1]
    f_finalchar= f_char + f_char2
    output_2[f_finalchar] = word

print("output2 :", output_2)