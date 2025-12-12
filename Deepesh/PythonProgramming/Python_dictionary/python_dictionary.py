"""
# Properties:
-> Dictionary is mutable data type, we can modify the data at any point of time.
-> Dictionary contains data in keys value pair , e.g  {'key1': 'value1', 'key2': 'value2'}
-> Dictionary allows unique keys only, duplicate keys are not allowed.
   e.g.  {'a': 123, 'b': 567, 'c': 789, 'a': 500}
   -> if user provide duplicate key, then it will consider the latest defined value.
-> Dictionary follows LIFO (last in first out)

-> Dictionary allows only immutable data type as key, e.g. int, float, complex, str, tuple, boolean.
-> There is no restriction for of the dict data type.
"""

dict1 = {'a': 123,
         10 : [3, 4, 5],
         6.7 : (4, 6, 8),
         (1, 2, 3) : {'P':11, 'Q':22},
         True : {3, 5, 7, 8},
         'a': 500,
         # [1, 0, 2] : 'Python' # TypeError: unhashable type: 'list'
         # {4, 6, 8} : {'a': 33} # TypeError: unhashable type: 'set'
         }

print(dict1, type(dict1))
# {'a': 500, 10: [3, 4, 5], 6.7: (4, 6, 8), (1, 2, 3): {'P': 11, 'Q': 22}, True: {8, 3, 5, 7}} <class 'dict'>

# get dict data with key
print(dict1[10])  # [3, 4, 5]
print(dict1[10][1]) # 4
print(dict1[(1, 2, 3)]) # {'P': 11, 'Q': 22}
print(dict1[(1, 2, 3)]['Q']) # 22

print("#"*50)
###########################
# apply loop on dict
dict2 = {'x': 22, 'y': 33, 'z': 44}
for k, v in dict2.items():
    print("key :", k, "value :", v)
    #print(k)

"""
key : x value : 22
key : y value : 33
key : z value : 44
"""

print("_"*50)
for k in enumerate(dict2):
    print(k)

"""
(0, 'x')
(1, 'y')
(2, 'z')
"""

print("_"*50)
############################################
print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'