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

dict1= {'a': 123,10:[3,4,5],6.75 : (2.5,4.7),(1,2,3):{'p':111, 'q':222},False:{1,2,3}}
print(dict1, type(dict1))

# get dict data with key
print(dict1[10])
print(dict1[10][2])
#print(dict1[10][4])- when 2nd index added value doesnt exist, it doesnt print it ,ignores it
print(dict1[(1,2,3)])
print(dict1[(1,2,3)]['q'])


# apply loop on dict
dict2 = {'x': 222, 'y': 333, 'z': 444}
for k, v in dict2.items():
    print("key :", k, "value :", v)
    print(k)