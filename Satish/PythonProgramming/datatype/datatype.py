"""
1. Number
    i) integer
    ii) float
    iii)complex

2. Sequential
    i) string
    ii)list
    iii)tuple

3. Dictionary
4.Set
5.Boolean

"""

##########Integer###############

a=1
b=564
c=12345678
print("a:",a,type(a)) #1 <class 'int'>
print("b:",b,type(b)) # 564 <class 'int'>
print("c:",c,type(c)) # 12345678 <class 'int'>

print('_'*50)

########float#################
a=0.1
b=5.432
c=12345.5678
print("a:",a,type(a)) #0.1 <class 'float'>
print("b:",b,type(b)) # 5.432 <class 'float'>
print("c:",c,type(c)) #12345.5678 <class 'float'>

###complex######
a=2+10j
print("a:",type(a)) #a: <class 'complex'>
print("realnumber",a.real) #realnumber 2.0
print("imaginary number",a.imag)#imaginary number 10.0

print('_'*50)

#####string################
# Anything enclosed in single ,double  or triple quote is called string.
a='satish'
b="jyoti"
c=""" satish
kumar paliwal 
"""
print("a:",a,type(a)) # a: satish <class 'str'>
print("b:",b,type(b)) # b: jyoti <class 'str'>
print("c:",c,type(c))
""" 
c:  satish
kumar paliwal 
 <class 'str'>

"""
###string follows positive and negative indexing#####

str1= "JYOTI PALIWAL"

"""
    0   1   2   3   4  5   6   7   8   9   10  11 12 POSITIVE INDEXING
    J   Y   O   T   I      P   A   L   I   W   A   L
   -13-12  -11 -10 -9  -8  -7 -6  -5  -4  -3   -2  -1 NEGATIVE INDEXING
 
"""

print(str1[0])
print(str1[-13])
print(str1[12])
print(str1[-1])
