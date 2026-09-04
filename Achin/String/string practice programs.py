#odd length in upper case and even length in lower case
'''
str = "India iS BesT country in the world"

wordlist = str.split(" ")
print(wordlist)
word = ""

for word in wordlist:
    if len(word) % 2 != 0:
        word = word.upper()
    else:
        word = word.lower()

    print(word)
'''
from Deepesh.PythonProgramming.Python_String.String_Programs import word_list

'''

#second largest word
str6 = "Everything is possible with hard work"
wordlist=str6.split(" ")
print(wordlist)

largst_word = ""
largst_len = 0
secondlargestword=[]
for word in wordlist:
    if len(word) > largst_len: # 3 > 2 | 8 > 3 | 6 > 8 | 11 > 8
        largst_len = len(word) # 2, 3, 8, 11
        largst_word = word # We, Are, Learning, Programming
    else:
        secondlargestword.append(word)

secondlargst_word = ""
secondlargst_len = 0
for secondlargest_word in secondlargestword:
     if len(secondlargest_word) > secondlargst_len: # 3 > 2 | 8 > 3 | 6 > 8 | 11 > 8
        secondlargst_len = len(secondlargest_word) # 2, 3, 8, 11
        secondlargst_word = secondlargest_word

print("secondLargest word and secondlargest len:", secondlargst_word, secondlargst_len)

print("Largest word and largest len:", largst_word, largst_len)
#print(secondlargestword)
'''
#python reverse string if it,s length is a multiple of 4

str="Hello Worldd"

if len(str)% 4== 0:
    print(str[::-1])

#count occurences of substring
str1="hi my name is achin hi"
print(str1.count("hi"))

# smallest word in string

str="hi i am achin"

word_list=str.split(" ")
print(word_list)
min=word_list[0]
for word in word_list:
    if len(word)<len(min):
        min=word
    else:
        continue

print(min)


