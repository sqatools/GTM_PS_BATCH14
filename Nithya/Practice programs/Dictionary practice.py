#Home Work Python code to generate dictionary output from given string.

str2 = "Hello we Are Learning Python"
# expected output1 = {'Ho': 'Hello', 'we': 'we', 'Ae': 'Are', 'Lg': 'Learning', 'Pn': 'Python'}

Output={}
words= str2.split(" ")
print("splitted:",words)
for word in words:
    blend1=word[0]+word[-1]
    Output[blend1] = word


print("Output :", Output)
print("*"*30)

d1= {'a':10, 'b':56, 'c':68}
print(sorted(d1))
val=sorted(d1.items()) #-------------- to get the dict format of key and value 

print("In dict format:",dict(val))