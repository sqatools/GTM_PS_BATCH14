#1)-----Write a Python program to get a string made of the first and the last 2 chars from a given string.
#If the string length is less than 2, return instead of the empty string
#Take a string as input.
# If the string consists of only 2 characters print True if
# not get a string made of the first and last 2 characters using indexing.
# Print the output.

print("_"*40)
str_01="hitest"
if len(str_01)<2 :
    print("true")
else:
    print(str_01[0:2]+str_01[-2:])


#2)In this program, we will take a list of strings as input and returns the length of the longest string.
#Steps to solve the program
#Take a list of strings as input.
#Create a variable named temp and assign its value equal to zero.
#Use for loop to iterate over each string of the list.
#Check if the length of the string is greater than the temp value, if yes assign the length of that string to the temp variable.
#Print the length of the longest string.

print("_"*40)
l1=["test","salesforce", "python", "selenium"]
longlength_l1=0
for word in l1:
    if len(word)>longlength_l1: #(4>0) (10>4) (6>10)
        longlength_l1=len(word)
print(longlength_l1)

#shortest length

print("_"*40)
l2=["salesforce", "testt", "python", "selenium"]
shortlength_l2=l2[0]
for word in l2:
    if len(word)<len(shortlength_l2):
        shortlength_l2=word

print(shortlength_l2)


print("_"*40)
print(longlength_l1)
str1 = "hi all i am learning python programming"
world_ls=str1.split(" ")
print(world_ls)
largest_word=" "
largest_len=0
for word in world_ls:
    if len(word)>largest_len:
        largest_len=len(word)
        largest_word=word
    else:
         continue

print(largest_len, largest_word)





#q1 : write a python program to count total vowels from given string.


"""
str2 = "helloieuE"
vowel = "aeiou"
count = 0
for char in str2:
    if char.lower() in vowel:
        count+=1
    else:
        continue
print("print the count of the vowels :", count)
"""

"""
#q2- write a program to remove duplicate character from the given string n generate output.

str3 = "hello friends i am learning python"
output = " "
for char in str3:
    if char not in output:
        output = output + char
    else:
        continue
print(output)

"""
"""
#q3 - write a program to remove duplicate words

str3 = "soumya pavan shruthi soumya aadhya aadhya"
word_list=str3.split()
print(word_list)
output=""
for word in word_list:
    if word not in output:
        output = output + " " + word
    else:
        continue
print(output)

# using set 

set_list = set(word_list)
print(set_list)
"""

"""
#write a python program to convert odd length word in upper cas n even length word in lower cas)

str5 = "India iS Best country in the world"
w_list = str5.split()
print(w_list)
for word in w_list:
    if len(word)%2==0:
        print(word.lower())
    else:
        print(word.upper())
"""
 # write a program to get 2nd largest word from given string
str6 = "Everything is possible withyuiut hard work"
w_list = str6.split()
print(w_list)
larg_word=""
second_word=""
for word in w_list:
    if len(word)>len(larg_word):
        larg_word=word
        print(larg_word)
    if len(word)>len(second_word) and len(word)<len(larg_word):
        second_word=word
        print(second_word)
    else:
        continue
print(second_word)


out = []
print("_"*40)
l4 = [1, 4, 6, 8]
for word in l4:
    if word%2==0:
        out.append(word)
    else:
        continue
print(out)



