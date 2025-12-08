s5="india is BesT country in the world"
s6=s5.split(" ")
print(s6)
new=""
l1=0
for word in s6:
    if(len(word)%2==0):
        word=word.lower()
        new = new+word+" "
    else :
        word=word.upper()
        new = new+word+" "

print(new)

'''Q5write a python Program to convert odd length word in uppercase & even length  lower case 
Q6 :  write a python Program to get second-largest word from given string.
str6 = "Everything is possible with hard work"
output = "possible"
'''
print("_"*50)
str6 = "Everything is possible with hard work"
word_list=str6.split(" ")
print(word_list)
lar1=""
lar2=""
len1=0

for word in word_list:
    if len(word) > len(lar1):
        lar2 = lar1
        lar1 = word
    elif len(word) > len(lar2) and word != lar1:
        lar2 = word
print(lar2,len(lar2))
print("_"*50)
