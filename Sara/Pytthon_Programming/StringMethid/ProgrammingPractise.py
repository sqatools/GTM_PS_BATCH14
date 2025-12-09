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