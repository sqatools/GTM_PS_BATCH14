#Write a program to count total vowels from given string
print("-"*15, "Program 1","-"*15)
s1="We are learning python programming"
s2=['a','e','i','o','u']
count = 0
for i in range (0,len(s1),1):
    if s1[i] in s2:
        count +=1
    else:
        continue
print("Total vowels using 1 way:", count) # Total vowels using 1 way: 10

##### second way for program 1
s1="We are learning python programming"
s2=['a','e','i','o','u']
count = 0
for char in s1:
    if char in s2:
        count +=1
    else:
        continue
print("Total vowels using 2nd way:", count) # TTotal vowels using 2nd way: 10

print()
##################################################################
# Write a python program to remove duplicate char from given string
print("-"*15, "Program 2","-"*15)
s1="We are learning python programming"
output=""
# output- We arlnigpythom
for char in s1:
    if char in output:
        continue
    else:
        output= output+char
print(output) # We arlnigpythom

print()
##################################################################
# Write a python program to remove duplicate char from given string
print("-"*15, "Program 3","-"*15)
s1="Hello Hello People. Good Morning People"
output1=""
s2= s1.split(" ")
print(s2)
for char in s2:
    if char in output1:
        continue
    else:
        output1=output1+char+" "
print(output1) #Hello People. Good Morning

print()
##################################################################
# Write a program to get the largest word from the given statement 44:11

