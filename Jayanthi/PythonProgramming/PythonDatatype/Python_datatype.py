""" python variable """
#int,float complex

n1=0
n2=1
n3=1.00
n4=787878878878787
n5=34.909
n6=67.05
n7=10+20j
n8=20+30j
print("n1=",n1,type(n1))
print("n2=",n2,type(n2))
print("n3=",n3,type(n3))
print("n4=",n4,type(n4))
print("n5=",n5,type(n5))
print("n6=",n6,type(n6))
print("n7=",n7,type(n7))
print("real number:",n7.real)
print("img number:",n7.imag)
print("n8=",n8,type(n8))
print("real number:",n8.real)
print("imag number:",n8.imag)

# String

s1=""
s2="Hello"
s3="Hi"
s4="testing the python ,The word 'forest' " \
    "conjures a powerful image: a deep, hushed cathedral of green, sunlight filtered"
s5="""The word "forest" conjures a powerful image: a deep, hushed cathedral of green, 
sunlight filtered into emerald beams, and the pervasive scent of damp earth and living wood. 
More than just a collection of trees, a forest is a colossal, intricate, self-regulating ecosystem—the 
very lungs and green heart of our planet. It is a living testament to biological complexity, a critical 
buffer against climate change, and the wellspring of life for countless species, including our own. 
To understand the forest is to understand the indispensable engine that makes Earth habitable"""
s6="Janvika"

print("s1=",s1,type(s1))
print("s2=",s2,type(s2))
print("s3=",s3,type(s3))
print("s4=",s4,type(s4))
print("s5=",s5,type(s5))
print("s6=",s6,type(s6))

"""
  0  1  2  3  4  5  6  +ve indexing
  J  A  N  V  I  K  A
 -7  -6 -5 -4 -3 -2 -1  -ve indexing
 """
print(s6[0])
print(s6[-6])
print(s6[(-2)**2])

# List:

list1=[5,1.1,3+5j,(9,1.1,'hello'),{'a':125,'b':'hello'},False]
print(list1,type(list1))

print(list1[-1])
print(list1[5])
print(list1[3][2])
print(list1[3][2][3])
# print(list1[4][1]) #: Since it was not sequence

list2=[1,2,3]
# list2.append([100,200])
print(list2)

# Tuple

tup2=(6,1.5,3+6j,(9,1.1,'hello'),{'a':125,'b':'hello'},True)
print(tup2)

print(tup2,type(tup2))

print(tup2[-1])
print(tup2[5])
print(tup2[3][2])
print(tup2[3][2][3])
"""
not able mutable
tup3=(1,2,3)
tup3.append(100)
print(tup3)"""

# Dictionary

dict1={'a':125,'1.1':3+6j,'p':[1,2,3]}
print(dict1,type(dict1))

print(dict1['a'])
print(dict1['1.1'])
dict1['a']=500 # to append
print(dict1)

dict2 = {100: 'Hello',
         5.5 : [3, 5, 7],
         45+5j: (6, 9, 0),
         'abc': {'a': 123, 'b': 678},
         (1, 2, 3): {5, 8, 9, 12, 5},
         True: 345,
          #[4, 6, 7] : 7567  # TypeError: unhashable type: 'list' key value can t be list
         }
print(dict2)

# Set : only unique value and random key
set1={1,1.1,3.45,'python',3+10j,'python'}
print(set1,type(set1))

#set2 = {12, 13, 5, 'Python', (4, 6, 8), True, 5.7, 7+34j, 5, {3, 5, 7}} set inside set does not work
#print(set2)
#boolean
a=5
b=6
c=5
print(a==b)
print(a==c)
