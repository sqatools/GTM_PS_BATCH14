"""
# Properties:
-> Dictionary is mutable data type, we can modify the data at any point of time.
-> Dictionary contains data in keys value pair , e.g  {'key1': 'value1', 'key2': 'value2'}
-> Dictionary allows unique keys only, duplicate keys are not allowed.
   e.g.  {'a': 123, 'b': 567, 'c': 789, 'a': 500}
   -> if user provide duplicate key, then it will consider the latest defined value.
-> Dictionary follows LIFO (last in first out) # suppose we put something in box then last item we can take out first

-> Dictionary allows only immutable data type as key, e.g. int, float, complex, str, tuple, boolean.
-> There is no restriction for of the dict data type for value.
-> Dictionary doesn't follow indexing so we find value of dictionary by giving their key as indexing
"""
# get dict data with key
dict1={1:'a',5.2:'hello',5+3j:[1,2,3],'python':5,(1,2,3):{'a':123,'b':[1,2,3]}}
print(dict1,type(dict1))
print(dict1[1]) # a
print(dict1[5.2]) #hello
print(dict1[5+3j]) # [1, 2, 3]
print(dict1[5+3j][1]) # 2

#apply loop on dictionary
dict2={'a':11,'b':22,'c':33,'d':44}
for key,value in dict2.items():   # items is a method
    print('key:',key,'value:',value)
print(dict2.items())  # dict_items([('a', 11), ('b', 22), ('c', 33), ('d', 44)])

"""
key: a value: 11
key: b value: 22
key: c value: 33
key: d value: 44
"""
print("_"*50)
#method in dictionary
print(dir(dict))

"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

"""