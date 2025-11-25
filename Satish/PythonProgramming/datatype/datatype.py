"""
1. Number
    i) integer
    ii) float
    iii)complex

2. Sequential  Only sequential data type follow positive and negative sequencing
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



#### list data type

lst1= [1,2.34,[1,2,3],(2,3,4),True,'python',{2,3,4},{'key1':35}]
print(lst1)
lst2=[1,2,3,4]
print(lst2)
lst3=[2.34,3,5]
print(lst3)

### Tuple data type same as list except list is mutable and tuple is imutable
tup1=(1,2,3)
print(tup1)
tup2=(1.23,4,'python')
print(tup2)
tup3=('satish',{1,2,3},{'key2':45},[1,2,3])
print(tup3)

##dictionary data type###
# it is a mutable data type
#Dictionary contains data in keys value pair , e.g  {'key1': 'value1', 'key2': 'value2'}
#Dictionary allows only immutable data type as key, e.g. int, float, complex, str, tuple, boolean
#There is no restriction of value of the dict data type

dict1={1:[1,2,3]}
print(dict1)
dict2={'satish':{1,2,3}}
print(dict2)
dict3={2.34,'python'}
print(dict3)

##Bolean data type
#Boolean is immutable data type
#Boolean is output of any of the condition.

a=True
print(a)
b=False
print(b)
a=30
b=40
c=30
print(a==c)
print(a==b)

##set data type
#Set is mutable data type, we can modify it at any point of time.
#Set only allows immutable type as member, int, float, complex, string, tuple, boolean.
#Set only contains unique values, duplicate values are not allowed.
set1={1,2,3}
print(set1)
set2={'python',2+3j,2.34,True,4}
print(set2)