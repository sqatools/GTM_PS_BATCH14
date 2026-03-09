
print("_"*50)
#################### convert string into raw string #########
# \t : add space in string
# \n :  add next line in string.

str_b = r"Hello \t\t we are \n Learning Python"
print(str_b)  # Hello \t\t we are \n Learning Python

str_c = r"c:\nov\tools"
print(str_c)  # c:\nov\tools

print("_"*50)
############################# Slicing #############
# Rule1 : str[start index:  end index]
"""
->  In this rule it will always get output from left to right.
->  default start index value is 0
->  default end index value is end of string.
->  start index and end index could be positive negative.
->  Output will include the start index value and exclude end index value
"""

str_d = "Python Programming"
print(str_d[0:6]) # Python
print(str_d[-11:-1]) # Programmin

# consider default end value
print(str_d[-11:])  # Programming
print(str_d[0:-11]) # Python
print(str_d[-15:-11]) # hon
print(str_d[0:10]) # Python Pro


print("_"*50)
# Rule2 : str[start index:  end index: step value]
"""
-> In this rule, output will include start index value and exclude end index value
-> default start index is zero (0) if step value is +ve
-> default start index is -1 if step value is -ve
-> default end index will be end of string if step value is +ve
-> default end index will be start of string if step value is -ve
"""

s1 = "Learning Python If fun"
print(s1[0:5:1]) # Learn
# get alternate characters
print(s1[0:22:2]) # Lann yhnI u

# default start value as zero as step value is +ve
print(s1[:11:1])  # Learning Py

# default start value as -1 as step value is -ve
print(s1[:11:-1])

# default end index will be end of string if step value is +ve
print(s1[2::1])  # arning Python If fun

#  default end index will be start of string if step value is -ve
print(s1[-7::-1]) # nohtyP gninraeL
print(s1[7::-1]) # gninraeL

# reverse the entire string
s2 = "Good Morning"
print(s2[::-1]) # gninroM dooG
print(s2[-1:-len(s2)-1:-1])  # gninroM dooG

print(s2[::1])  # Good Morning

# print all the character except first and last
print(s2[1:-1]) # ood Mornin

# Homework slicing
str3 = "Virat is Best Batsman of India"
# output1 = "VViratt iiss BBestt BBatsmann ooff IIndiaa"
# output2 = "airat is Best Batsman of IndiV"
# output3 = "tiraV si tesB natsmaB fo andiI"


print("_"*50)
################ Apply loop on string ###############
str10 = "Learning Python"

# loop without indexing
for char in str10:
    print(char)

print("_"*50)
# loop with indexing
for i in range(0, len(str10), 1):
    print(i, str10[i])

print("_"*50)
for i, char in enumerate(str10):
    print(i, char)