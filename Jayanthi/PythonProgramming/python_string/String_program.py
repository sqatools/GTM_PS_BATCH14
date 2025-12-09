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







