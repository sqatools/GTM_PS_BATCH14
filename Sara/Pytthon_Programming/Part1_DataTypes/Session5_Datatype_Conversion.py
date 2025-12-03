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