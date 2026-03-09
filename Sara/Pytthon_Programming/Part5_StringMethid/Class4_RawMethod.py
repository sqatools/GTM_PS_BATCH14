#***************Raw Method ************
print("-"*15,"Raw Method","-"*15)

'''
s1="\S\abc" # SyntaxWarning: "\S" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\S"? A raw string is also an option.
     #        s1="\S\abc"
print(s1) # \Sbc
'''

s1=r"s\abc"
print(s1) # s\abc