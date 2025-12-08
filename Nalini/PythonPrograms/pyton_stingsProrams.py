"""
str="hello world hi"
vowels = "aeoiu"
count=0
for char in str:
    if char in vowels:
        count+=1
    else:
        continue
print("no of voewls: ", count)
"""
"""
str = "hello world"
output =""
for char  in str:
    if char not in  output:
        output=  output + char
    else:
        continue
print(output)
"""
"""
str = "we are learning python programming"
wordlist = str.split(" ")
word = ""
newlist=""
for word in wordlist:
    if len(word)%2==0:
        newlist= newlist + word.upper() + " "
    else:
        newlist = newlist + word.lower() + " "
print(newlist)

"""
"""
 Q6 :  write a python Program to get second-largest word from given string.
str6 = "Everything is possible with hard work"
output = "possible"
"""
str = "Everything is possible with hard work"
wordlist = str.split(" ")
larg_word = " "
slarg_word = " "
largest=" "
for word in wordlist:
    if len(word) > len(larg_word):
        larg_word = word

    if len(word) > len(slarg_word) and len(word) < len(larg_word):
        slarg_word = word

    else:
        continue

print(larg_word, slarg_word)






