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
# Write a program to get the largest word from the given statement
print("-"*15, "Program 4","-"*15)
s1="Hello. Good Morning People"
r1=s1.split(" ")
print(r1)
lar_word=" "
lar_len= 0
for char in r1:
    if (len(char))> lar_len:
        lar_len=len(char)
        lar_word= char
    else:
        continue
print("Largest length is:",lar_len,"Word is:",lar_word)

print()
##################################################################
# Write a program to print odd length work in upper case and even length word in lower case
print("-"*15, "Program 5","-"*15)
s1="India iS BesT country in the world"
w1=s1.split(" ")
print(w1)
ew=""
o1=""
ow=""
result1=[]
for char in w1:
    if len(char)%2==0:
        ew=char.lower()
        #print(ew)
    else:
        ew=char.upper()
        #print(ew)
    #result1.append(ew)
    ow= ow +(" ") + ew

#print(result1)
print(ow.strip()) # INDIA is best COUNTRY in THE WORLD

print()
##################################################################
# Write a program to get second largest word from the given string
print("-"*15, "Program 6","-"*15)
s1="Everything is possible with hardwork"
s2=s1.split(" ")
s3=[ ]
lw=''
slw=''
print(s2)
for char in s2:
    if len(char)>len(lw):
        lw= char
        #print('a',lw)
    if len(char)>len(slw) and len(char)< len(lw):
        slw=char
        #print('d', slw)
    else:
        continue
print("Second largest word is: ", slw)


