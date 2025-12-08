#1)-----Write a Python program to get a string made of the first and the last 2 chars from a given string.
#If the string length is less than 2, return instead of the empty string
#Take a string as input.
# If the string consists of only 2 characters print True if
# not get a string made of the first and last 2 characters using indexing.
# Print the output.

"""
s1 = "soumya"
if len(s1)<2 :
    print("true")
else :
    print(s1[0:2]+s1[-2:])

"""

#----2)

string = ["i", "am", "learning", "python"]
temp = 0

for word in string:
    a = len(word)
    if a > temp:
        temp = a

#Printing output
print(temp)

for test in string:
    a = len(test)
