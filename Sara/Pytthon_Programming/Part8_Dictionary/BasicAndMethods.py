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
