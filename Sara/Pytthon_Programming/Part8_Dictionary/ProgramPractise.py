print("*"*15,'Program 1', "*"*15)
print(" Python code to generate dictionary output from given string.")

str1 = "Hello we Are Learning Python"
# expected output1 = {'H': 'Hello', 'w': 'we', 'A': 'Are', 'L': 'Learning', 'P': 'Python'}

result1={}
word_list=str1.split(" ")
print(word_list) # ['Hello', 'we', 'Are', 'Learning', 'Python']
for i in word_list:
    f_word=i[0]
    result1[f_word]= i
print('result1 :', result1) # result1 : {'H': 'Hello', 'w': 'we', 'A': 'Are', 'L': 'Learning', 'P': 'Python'}

print()
###################################################################
print("*"*15,'Program 2', "*"*15)
#Home Work Python code to
print(" Generate dictionary output from given string. ")

str2 = "Hello we Are Learning Python"
# expected output1 = {'Ho': 'Hello', 'we': 'we', 'Ae': 'Are', 'Lg': 'Learning', 'Pn': 'Python'}
result2={}
word_l=str2.split(" ")
# print(word_l)

for i in word_l:
    for j in i:
        f_w2=j[-1]
    f_w1 = i[0]
    s1=f_w1+f_w2

    result2[s1]=i
print('Result 2:', result2) # Result 2: {'Ho': 'Hello', 'we': 'we', 'Ae': 'Are', 'Lg': 'Learning', 'Pn': 'Python'}