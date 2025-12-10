# q1 :  write a python program to count total vowels from given string.
str1="Hello we are LeArning PythOn"
vowels="aeiou"
count=0
for i in str1:
    if i.lower() in vowels:
        count +=1
    else:
        continue
print("number of vowels:",count)

print("#"*50)
# q2 :  write a python program remove duplicate character from given string and generate output.
str2="Hello we are LeArning PythOn"
output=""
for char in str2:
    if char not in output:
        output=output+char
    else:
        continue
print(output)
print("#"*50)
#q3 :  write a python program remove duplicate words from given string and generate output.
str3 = "Mona Pavan Achin Anshika Pavan Achin Mona"
output=""
worklist=str3.split()
for word in worklist:
    if word not in output:
        output=output+word+" "
    else:
        continue
print(output)

print("#"*50)
############################################
#q4 :  write a python program get largest word from given string.
length=0
largest_word=""
str4 = "We Are Learning Python Programming and its Fun"
worklist =str4.split()
for char in worklist:
    if len(char)>length:
        length=len(char)
        largest_word=char
    else:
        continue
print("Largest word:",length,largest_word)

#Q5 write a python program to convert odd length word in upper case and even length word in lower case.
str5 = "India iS BesT country in the world"
# output = "INDIA is best COUNTRY in THE WORLD"
ul=""
wordlist=str5.split()
for word in wordlist:
    if len(word)%2==0:
        up=word.lower()
    else:
        up=word.upper()
    ul=ul+up+" "
print(ul)


# Q6 :  write a python Program to get second-largest word from given string.
str6 = "Everything is possible with hard work"
output = "possible"

word_list1=str6.split(" ")
print(word_list1)
large_word =""
lar_len=0
Sec_lar_word=""
sec_len=0
for word in word_list1:
    if len(word)>lar_len:
        lar_len=len(word)
        large_word=word
    if len(word) >sec_len and len(word) < lar_len:
        sec_len=len(word)
        Sec_lar_word=word
    else:
        continue
print("Largest length:",large_word,lar_len)
print("Second largest :",Sec_lar_word,sec_len)

# 1). Write a Python program to get a string made of the first and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string
print("-"*50)
char1="Janvika"
if len(char1)<2:
    print("True")
else:
    print(char1[:2]+char1[-2:])
# 2). Python string program that takes a list of strings and
# returns the length of the longest string.
print("-"*50)
char2="Janvika is good and Brilliant girl"
leng_lar=0
list1=char2.split()
for i in list1:
    if len(i)>leng_lar:
        leng_lar=len(i)
    else:
        continue
print("Largest Lenth",leng_lar)

# 3). Python string program to get a string made of 4 copies of the last two
# characters of a specified string (length must be at least 2).
print("-"*50)
print(char1[-2:]*4)

# 5). Python string program to count occurrences of a substring in a string.
print("-"*50)
str10="sqatoolspythonspy"
sub="spy"
print(str10.count("spy"))

#6). Python string program to test whether a passed letter is a vowel or consonant.
print("-"*50)
str11="testing"
vowel="aeiou"
test=str11.lower()
for i in test:
    if i in vowel:
        print("Vowel:",i)
    else:
        print("Consonant:",i)
        continue
# 7). Find the longest and smallest word in the input string.
print("-"*50)
len1=0
long_word=""
short_word=""
str12="Janvika is child of Jayanthi"
char3=str12.split()
for i in char3:
    if len(i)>len1:
        len1=len(i)
        long_word=i
    if len(i)<len1:
        sec_len=len(i)
        short_word=i
    else:
        continue
print("Largest length:",len1,long_word)
print("Largest length:",sec_len,short_word)

# 8). Print most simultaneously repeated characters in the input string.
print("-"*50)
str15="Hellllllllllllllllllllllo Worrrrrrrrrrrrrrrd"
repeat_count=0
repeat_char=""
temp=1
for i in range(len(str15)-1):
    if str15[i]==str15[i+1]:
        temp=temp+1
        if temp > repeat_count:
            repeat_count=temp
            repeat_char=str15[i]
    else:
       temp=1

print(repeat_count,repeat_char)



















