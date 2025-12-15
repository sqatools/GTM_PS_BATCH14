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


dic_1 = {'a': 365,
         12 : [1, 2, 5],
         0.5 : (10, 1, 58),
         (1, 2, 3) : {'P':21, 'Q':32},
         True : {1,2,3},
         'a': 500}

print(dic_1[12])
print("#"*30)
#loop on dictionary

dic_2 = {'q': 12, 'r': 22, 's': 32}

for i,j in (dic_2.items()):
    print(i , j)
# dic functions
print("#"*30)
#clear dictionary
a= dic_2.items()

b=dic_2.clear()
print (a,b)


