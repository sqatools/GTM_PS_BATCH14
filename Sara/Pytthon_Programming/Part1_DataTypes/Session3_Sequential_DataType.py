#***************** SEQUENTIAL **************************

"""
1. String
2. List
3. Tuple
"""
#***************** String **************************
print("-"*30, "Sequential","-"*30)
print("-"*15, "String","-"*15)
print("")
a='Hello'
b="Python"
c='''Python learning'''
d="""HI, How are you?"""
print("value for single quote:",a,type(a)) #value for single quote: Hello <class 'str'>
print("value for double quote:",b,type(b)) #value for double quote: Python <class 'str'>
print("value for single triple quote:",c,type(c)) #value for single triple quote: Python learning <class 'str'>
print("value for double triple quote:",d,type(d)) #value for double triple quote: HI, How are you? <class 'str'>
print("")

#***************** Paragraph string **************************

e="Hi, Good Morning. Double quote in single line" #Hi, Good Morning. Double quote in single line
print(e,)
print("")

f= """Triple quote check
2 line code"""
print(f)
#Triple quote check
#2 line code

print("")
g='''Single quote check
for more than 1 line string'''
print(g)
#Single quote check
#for more than 1 line string

h = "Hello, we are learning Python. " \
    "When you press enter you will get blackslash which mean it will print in single line."

print(h, type(h))
# Hello, we are learning Python. When you press enter you will get blackslash which mean it will print in single line. <class 'str'>

#**********POSITIVE and NEGATIVE INDEXING ***************
print("")

c1="HelloWorld"
'''
  0  1  2   3  4  5  6  7  8  9  --postive indexing
  H  e  l   l  o  W  o  r  l  d
-10 -9 -8- -7 -6 -5 -4 -3 -2 -1   --negative indexing

'''
print(c1[2]) # l
print(c1[-5]) # W
'print(str[c1]) # incorrect. will not print anything'
print(str(c1)) # HelloWorld

#***************** List **************************
print("")
print("-"*15, "List","-"*15)


