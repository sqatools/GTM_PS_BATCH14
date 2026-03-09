#DataType conversion

#********* INT TO OTHERS **********
print("-"*15,"Int to Other Datatype","-"*15)
a1=5
a2= float(a1)
a3= complex(a1)
a4=str(a1)
#a5=list(a1) list,tuple,set,dict all same error
#a6=boolean(a1)
print(a1, type(a1)) #5 <class 'int'
print(a2, type(a2)) #5.0 <class 'float'>
print(a3, type(a3)) #(5+0j) <class 'complex'>
print(a4, type(a4)) #5 <class 'str'>
#print(a5, type(a5)) #TypeError: 'int' object is not iterable
#print(a6, type(a6)) #NameError: name 'boolean' is not defined

#********* Float TO OTHERS **********
print("-"*15,"Float to Other Datatype","-"*15)

f1=66.66
print(int(f1)) #66

f3= complex(f1)
f4=str(f1)

print(f3, type(f3)) # (66.66+0j) <class 'complex'>
print(f4, type(f4)) # 66.66 <class 'str'>

'''
f5=tuple(f1)
print(f5, tuple(f5)) ## TypeError: 'float' object is not iterable

list,tuple,set,dict all same error

'''

#********* STRING TO OTHERS **********
print("-"*15,"String to Other Datatype","-"*15)

s1="Python"
s2="44"

"""
s3= int(s1)
print(s3) ValueError: invalid literal for int() with base 10: 'Python'
"""

s4=int(s2)
print(s4) # 44
