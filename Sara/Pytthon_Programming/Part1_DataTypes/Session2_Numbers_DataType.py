#***************** NUMBERS **************************

"""
1. Integer
2. Flaat
3. Complex
"""
#***************** INTEGER **************************
print("-"*30, "Number","-"*30)
print("-"*15, "Integer","-"*15)
var1=10
var2=200
var3=45676
var4=44.55
var5=2.333
var6=456.01
var7=67889754.3
print("value of var 1:", var1, type(var1)) #value of var 1: 10 <class 'int'>
print("value of var 2:", var2, type(var2)) #value of var 2: 200 <class 'int'>
print("value of var 3:", var3, type (var3)) #value of var 3: 45676 <class 'int'>
print("")

#***************** FLOAT **************************
print("-"*15, "Float","-"*15)
print("value of var 4:", var4, type (var4)) #value of var 4: 44.55 <class 'float'>
print("value of var 5:", var5, type (var5)) #value of var 5: 2.333 <class 'float'>
print("value of var 6:", var6, type (var6)) #value of var 6: 456.01 <class 'float'>
print("value of var 7:", var7, type (var7)) #value of var 7: 67889754.3 <class 'float'>
print("")

#***************** COMPLEX **************************
var8= 20+40j
print("-"*15, "Complex","-"*15)
print("value of var 8:", var8, type (var8)) #value of var 8: (20+40j) <class 'complex'>

var9 = 1 + 1j
print("value of var 9:", var9, type (var9)) #value of var 9: (1+1j) <class 'complex'>

'''
var10= 4+6t #this is incorrect complex. it will throw syntax error
print(var10) #SyntaxError: invalid decimal literal

var11= 1+j20
print(var11) # this will not print any value or throw error
'''
var12 = 10 + 1j
print("value of var 12:", var12, type (var12)) #value of var 12: (10+1j) <class 'complex'>
