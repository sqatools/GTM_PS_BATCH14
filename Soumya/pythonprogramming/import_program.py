# reverse a string without using reverse method
s1="testtest"
print(s1[::-1])

#Check Palindrome
print("*"*50)
s1="madam"
if s1==s1[::-1]:
    print("given string is palindrome")
else:
    print("given string is not palindrome")

#Count Occurrence of Each Character
print("*"*50)
s2="automation"
d={}
for ch in s2:
    if ch in d:
        d[ch]=d[ch]+1
    else:
        d[ch]=1
print(d)

#Find Duplicate Characters in String
s3="testtest"
dup=[]
for ch in s3:
    if s3.count(ch)>1 and ch not in dup:
        dup.append(ch)
print(dup)


#prime number
num1=16
count=0
for i in range(2, num1):
    if num1%i==0:
        count+=1
        break
    else:
        continue
if count>0:
    print("given number is not a prime number")
else:
    print("given number is a prime number")


##q1 :  write a python program to count total vowels from given string.

print("*"*50)
str1 = "Hello we are LeArning PythOn"
vowels="aeiou"
count=0
for ch in str1:
    if ch.lower() in vowels:
        count+=1
    else:
        continue
print(count)


#q2 :  write a python program remove duplicate character from given string and generate output.

print("*"*50)
str2 = "Hello we are LeArning PythOn"
output = ""
for ch in str2:
    if ch not in output:
        output=output+ch
    else:
        continue
print(output)

#q3 :  write a python program remove duplicate words from given string and generate output.
print("*"*50)
str3 = "Mona Pavan Achin Anshika Pavan Achin Mona"
output = "" #Mona Pavan Achin Anshika
wordlist=str3.split(" ")
for word in wordlist:
    if word not in output:
        output=output+word+" "
    else:
        continue

print(output)

#2nd approach
print("*"*50)
str3 = "Mona Pavan Achin Anshika Pavan Achin Mona"
word_list1=str3.split(" ")
print(word_list1)
set_result= set(word_list1)
print(set_result)
output=" ".join(set_result)
print(output)

print("#"*50)
############################################
#q4 :  write a python program get largest word from given string.

str4 = "We testestestressrtresdresdr Are Learning Pythontestesttest Programming and its Fun"
word_list=str4.split(" ")
largest_word=""
largest_leng=0
for word in word_list:
    if len(word)>largest_leng: #2>0
        largest_leng=len(word) #2,
        largest_word=word #we
    else:
        continue
print(largest_word, largest_leng)


###############################
#Q5 write a python program to convert odd length word in upper case and even length word in lower case.
str5 = "India iS BesT country in the world"
# output = "INDIA is best COUNTRY in THE WORLD"
word_list=str5.split(" ")
largest_word=""
largest_leng=0
for word in word_list:
    if len(word)%2==0:
        print("even length word in lower case:", word.lower())
    else:
        print("odd length word in upper case:", word.upper())

# Q1 : write a python program to get all even values from list

"""


print("*"*50)
output= []
list1 = [4, 5, 7, 8, 12, 17, 56]
for i in list1:
    if i%2==0:
        output.append(i)
print(output)

"""

# Q2 : write a python program to get all even and odd values with tag from list
# result = [(4, 'even'), (5, 'odd'), (7, 'odd'), (8, 'even'), (12, 'even')]
print("*"*50)
result= []
list1 = [4, 5, 7, 8, 12]
for i in list1:
    if i%2==0:
        result.append((i, "even"))

    else:
        result.append((i, "odd"))
print(result)


# get square of all value
print("*"*50)
list_2 = [5, 7, 8, 2, 9]
square=[i**2 for i in list_2]
print(square)




