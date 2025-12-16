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

#keys() method returns list of keys from dictionary.

dict3={'a':123,'b':222,'c':333}
print("list of keys",dict3.keys()) #['a', 'b', 'c']

#values() method returns list of values from dictionary.

dict3={'a':123,'b':222,'c':333}
print("list of values",dict3.values()) # [123, 222, 333]

## get method :  get method return the specific data with the help of key.

print(dict3.get('c')) #333

#items() methos returns list of key value
print(dict3.items()) #[('a', 123), ('b', 222), ('c', 333)]

# pop():  this method remove any specific key-value  from dict with the help of keys
dict4={1:'a',2:'b',3:'c'}
print(dict4.pop(2)) #b
print(dict4) #{1: 'a', 3: 'c'}

print("#"*50)
#popitem(): this method will remove key value pair from dict and return it. it will remove data from end of
# the dictionary.
dict5={1:'a',2:'b',3:'c'}
print(dict5.popitem()) #(3, 'c')
print(dict5) #{1: 'a', 2: 'b'}

print("_"*50)
#### Add data to dict ####
dict6={1:'a',2:'b',3:'c'}
dict6[4]='d'
print(dict6) #{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

print("#"*50)
###### Update method ####
# using this method we can update one dict data to another dictionary.
dict7={1:'a',2:'b',3:'c'}
dict8={4:'d',5:'e',6:'f'}
dict7.update(dict8)
print(dict7) #{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}

# clear method :  clear all the data from dictionary, only empty dict will remain.
dict7.clear()
print(dict7) #{}

 #remove variable from memory using "del"
del dict7#
#print("dict7 :", dict7)
# NameError: name 'dict7' is not defined

print("#"*50)
####################
# shallow copy: when we assign one dict data to another dict, and if modify any of the dict, then changes will
# reflect in both dictionary, then it is called shallow copy.

dict_i = {'x': 100, 'y': 200}
dict_j = dict_i
dict_j['z'] = 300
dict_i['w'] = 400

print("dict_i :", dict_i, id(dict_i)) # dict_i : {'x': 100, 'y': 200, 'z': 300, 'w': 400}
print("dict_j :", dict_j, id(dict_j)) # dict_i : {'x': 100, 'y': 200, 'z': 300, 'w': 400}


print("#"*50)
####################
# Deep copy: In this case we use copy method to copy data from one dict to another dict,
# and if modify changes in any of the dict, then it will reflect in another dict.
dict_1 = {'a': 111, 'b': 222}
dict_2 = dict_1.copy()
dict_2['c'] = 333
dict_1['d'] = 444
print("dict_1 :", dict_1, id(dict_1)) # {'a': 111, 'b': 222, 'd': 444}
print("dict_2:", dict_2, id(dict_2)) # {'a': 111, 'b': 222, 'c':
