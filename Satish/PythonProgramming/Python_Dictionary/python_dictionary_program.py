print("#"*50)
#######################################################################
#Home Work Python code to generate dictionary output from given string.

str2 = "Hello we Are Learning Python"
# expected output1 = {'Ho': 'Hello', 'we': 'we', 'Ae': 'Are', 'Lg': 'Learning', 'Pn': 'Python'}
word_list=str2.split()
dct_1={}
for word in word_list:
    fst_ch=word[0]
    lst_ch=word[-1]
    final_ch=fst_ch+lst_ch
    dct_1[final_ch]=word
print(dct_1) #{'Ho': 'Hello', 'we': 'we', 'Ae': 'Are', 'Lg': 'Learning', 'Pn': 'Python'}