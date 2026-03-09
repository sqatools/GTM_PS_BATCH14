a= "Hello, Work hard, work smart"
b= "THEY ARE GOOD"
c=  "Hello, Work hard, Work smart"
print("1.", a.upper())
print("2.", a.lower())
print("3.",a. isupper())
print("4.",b.isupper())
print ("5.", a. islower())
print("6.", a.title())
print("7.", a.count("work"))
print("8.", a.count("work" or "Work"))
print("9.", a.count("work" and "Work"))
print("10", c.count("work" or "Work"))
print("11", b.swapcase())
print("12.", a.swapcase())
print("13.",b.capitalize())
print("14.","Count of work:",a.count("work"),"Count of o:",a.count("o"))
print("15.", a.index('o'),a.index('work') )
print("16.", a.index('ork'))
print("17.", a.replace('work','Brain'))
print("18.", a.split())
print("19.", a.split('o'))
d= "friends".join(b)
print("20.",d )

print ("#"*50)

Input="India iS The Best CountRY in The WOrld"
Check= Input.split(" ")
print(Check)#Checking
Output=""
print("Output:", Output)#checking

for word in Check:
    if len(word)%2==0:
        Output= Output+word.upper()+" "
    else:
        Output= Output+word.lower()+" "
print("Output:", Output)

print("X"*50)
# # Q6 :  write a python Program to get second-largest word from given string.

Input="Indiaa iShjkhkjhh The Best CountRYIIII in The WOrld"
word_list= Input.split(" ")
lword = ''
slword = ''
for word in word_list:

    if len(word) > len(lword):
        slword = lword
        lword = word


    if len(slword) < len(word) < len(lword):
        slword = word
    else:
        continue


print("largest word :", lword)
print("second largest word:", slword)

print("#"*50)
#Python string program to reverse a string if it’s length is a multiple of 4.

str1= "Apple is my Favorite fruit in this Shopping"

a= str1.split()

for word in a:
    if len(word)%4==0:
        print(word[::-1], word)

print("X"*50)
#  Print most simultaneously repeated characters in the input string.
str2= "Apple is my Favorite fruuit in thiss Shopping baggg"
count=0
result1=""
result2=""
for char_1 in str2:
    rep_1=[char_1]
    #print("checking o/p:", rep_1)
    result1=rep_1
    if rep_1 in result1:
        result1= result1 + rep_1
        print("result1",result1)
        count+=1
    elif rep_1 in result1:
            result1 = result2
            print("result2", result2)


print("Final Output:", result1)

"""
Split words in Str2
Now split the char in each word of str2
check if the char in str2 is already available 
if yes add counter
if not continue
"""
#Write a Python program to calculate the length of a string with loop logic.
Str_3= "There are many flowers"
count=0
for word in Str_3:
    count=count+1
print(count,"Characters")

# Write a Python program to replace the second occurrence of any char with the special character $.

Input:Programming
wrd1=""
wrd2=""
for occ in Input:
    wrd1= wrd1+occ
    wrd2= wrd2
print("Two:", wrd2)













