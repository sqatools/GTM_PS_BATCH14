print(dir(dict))
'''
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', 
'__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', 
'__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

'''

print('-'*100)
dict1= {'a': 123, 'b': 'Hi', 'c': 545, 'd': 33}
print(dict1)

print('-'*100)
##########################################
# get dict data with key
dict2= {'a': 123, 'b': 'Hi', 'c': 545, 'd': 33, (1,2,3): {3,4}, 'e': {'r':1, 'a': 5}}
print(dict2)
print(dict2['d']) # 33
print(dict2[(1,2,3)]) # {3, 4}
print(dict2['e']['a']) # 5

print('-'*100)
##########################################

# apply loop on dict
dict3 = {'x': 22, 'y': 33, 'z': 44}
for i,j in dict3.items():
    print('key',i,'value',j)
'''
key x value 22
key y value 33
key z value 44
'''

print('-'*100)
##########################################

for k in enumerate(dict3):
    print(k)
'''
(0, 'x')
(1, 'y')
(2, 'z')
'''
#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

print('-'*100)
##########################################
print('*'*15,'Add Method', '*'*15)
d1={'a': 1, 'b': 2, 'c':3}
print(d1) # {'a': 1, 'b': 2, 'c': 3}
d1['d']=5
print('new', d1) # new {'a': 1, 'b': 2, 'c': 3, 'd': 5}

print('-'*100)
##########################################
print('*'*15,'Update Method', '*'*15)
d2={'a': 1, 'b': 2, 'c':3}
d3={'d': 1, 'e': 2, 'c':5}
d2.update(d3)
print(d2) # {'a': 1, 'b': 2, 'c': 5, 'd': 1, 'e': 2}
print(d3) # {'d': 1, 'e': 2, 'c': 5}

print('-'*100)
##########################################
print('*'*15,'Key and value Method', '*'*15)
d5={'a': 1, 'b': 2, 'c':3}

print('keys', d5.keys()) # keys dict_keys(['a', 'b', 'c'])
print('values', d5.values()) # values dict_values([1, 2, 3])

print('-'*100)
##########################################
print('*'*15,'get Method', '*'*15)

d12={'a': 1, 'b': 2, 'c':3}
v1=d12.get('c')
print(v1) # 3
print(d12) # {'a': 1, 'b': 2, 'c': 3}

print('-'*100)
##########################################
print('*'*15,'pop Method', '*'*15)

d7={'d': 1, 'e': 2, 'c':5}
print('pop', d7.pop('e')) # pop 2
print(d7) # {'d': 1, 'c': 5}

print('-'*100)
##########################################
print('*'*15,'pop item Method', '*'*15)

d8={'d': 1, 'e': 2, 'c':5}
v= d8.popitem()
print(v) # ('c', 5)
print(d8) # {'d': 1, 'e': 2}

print('-'*100)
##########################################
print('*'*15,'clear Method', '*'*15)

d9={'d': 1, 'e': 2, 'c':5}
v= d9.clear()
print(v) # None
print(d9) # {}

print('-'*100)
##########################################
print('*'*15,'shallow copy Method', '*'*15)
# d16 will only be a reference. memory address of d15 and d16 will be same
d15={'a': 1, 'b': 2, 'c':3}
d16=d15
print(d15) # {'a': 1, 'b': 2, 'c': 3}
print(d16) # {'a': 1, 'b': 2, 'c': 3}
print(id(d15)) # 2701659307200
print(id(d16)) # 2701659307200

d16['t']=8
d15['b']=4
print('new',d15) # new {'a': 1, 'b': 4, 'c': 3, 't': 8}
print('new',d16) # new {'a': 1, 'b': 4, 'c': 3, 't': 8}

print('-'*100)
##########################################

print('*'*15,'Deep copy Method', '*'*15)
# memory address of d17 and d18 will be different
d17={'a': 1, 'b': 2, 'c':3}
d18= d17.copy()
print(d17) # {'a': 1, 'b': 2, 'c': 3}
print(d18) # {'a': 1, 'b': 2, 'c': 3}
print(id(d17)) # 2362763607168
print(id(d18)) # 2362763607104

d17['t']=8
d18['b']=4
print('new',d17) # new {'a': 1, 'b': 2, 'c': 3, 't': 8}
print('new',d18) # new {'a': 1, 'b': 4, 'c': 3}

print('-'*100)
##########################################
print('*'*15,'del Method', '*'*15)

d10={'d': 1, 'e': 2, 'c':5}
del d10
# print(d10) # NameError: name 'd10' is not defined. Did you mean: 'd1'?

print('-'*100)
##########################################
print('*'*15,'Sorting Method', '*'*15)

dict_sort= {'a':4,'d':3,'b': 20,'c':5}
r1=sorted(dict_sort)
print("Sorting using key:", r1) # Sorting using key: ['a', 'b', 'c', 'd']

r2= sorted(dict_sort.items())
print("Sorting dict using key:", r2) # Sorting dict using key: [('a', 4), ('b', 20), ('c', 5), ('d', 3)]

r3= sorted(dict_sort.items(), key=lambda item:item[1])
print("Sorting dict using values:", r3) # Sorting dict using values: [('d', 3), ('a', 4), ('c', 5), ('b', 20)]

r4=sorted(dict_sort.items(), reverse=True)
print("Sorting in desc dict using key", r4) # Sorting in desc dict using key [('d', 3), ('c', 5), ('b', 20), ('a', 4)]

r5= sorted(dict_sort.items(), key=lambda item:item[1], reverse=True)
print("Sorting in desc dict using values:", r5) # Sorting in desc dict using values: [('b', 20), ('c', 5), ('a', 4), ('d', 3)]

print('-'*100)
##########################################
print('*'*15,'Sorting for same key', '*'*15)

dict_sort= {'a':4,'d':3,'a': 20,'c':5}
r6=sorted(dict_sort)
print("Sorting using key:", r6) # Sorting using key: ['a', 'c', 'd']

r7= sorted(dict_sort.items())
print("Sorting dict using key:", r7) # # Sorting dict using key: [('a', 20), ('c', 5), ('d', 3)]

dict_sort1= {'c':4,'d':3,'a': 4,'b':5}
r8= sorted(dict_sort1.items(), key=lambda item:item[1])
print("Sorting dict using values:", r8) # Sorting dict using values: [('d', 3), ('c', 4), ('a', 4), ('b', 5)]

