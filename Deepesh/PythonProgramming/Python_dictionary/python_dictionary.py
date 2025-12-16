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

print("_"*50)
#### Add data to dict ####
dict_a = {'a': 123, 'b': 345}
dict_a['c'] = 200
print("dict_a :", dict_a) # dict_a : {'a': 123, 'b': 345, 'c': 200}


print("#"*50)
###### Update method ####
# using this method we can update one dict data to another dictionary.
dict_b = {'P': 234, 'Q': 8767}
dict_c = {'name': 'Rahul', 'age': 25, 'email': 'rahul@gmail.com'}
print("dict_c :", dict_c)  # {'name': 'Rahul', 'age': 25, 'email': 'rahul@gmail.com'}

# update dict_b data to dict_c
dict_c.update(dict_b)
print("dict_c :", dict_c) # {'name': 'Rahul', 'age': 25, 'email': 'rahul@gmail.com', 'P': 234, 'Q': 8767}


print("#"*50)
####################
# get method :  get method return the specific data with the help of key.
dict_d = {'name': 'Rahul', 'age': 25, 'email': 'rahul@gmail.com', 'P': 234, 'Q': 8767}
email_val = dict_d.get('email')
print("email value :", email_val)  # email value : rahul@gmail.com

print("#"*50)
####################
# keys(), values():  These methods return list of keys and values.
dict_d = {'name': 'Rahul', 'age': 25, 'email': 'rahul@gmail.com', 'P': 234, 'Q': 8767}
print("list of keys :", dict_d.keys()) # ['name', 'age', 'email', 'P', 'Q']
print("list of values :", dict_d.values()) # ['Rahul', 25, 'rahul@gmail.com', 234, 8767]


print("#"*50)
####################
# pop():  this method remove any specific data from dict with the help of keys
dict_e = {'name': 'Rahul', 'age': 25, 'email': 'rahul@gmail.com', 'P': 234, 'Q': 8767}
val = dict_e.pop('age')

print("removed :", val)
print("dict_e :", dict_e) # dict_e : {'name': 'Rahul', 'email': 'rahul@gmail.com', 'P': 234, 'Q': 8767}

dict_e['P'] = 500
print("dict_e :", dict_e) # {'name': 'Rahul', 'email': 'rahul@gmail.com', 'P': 500, 'Q': 8767}


print("#"*50)
####################
# popitem(): this method will remove key value pair from dict and return it. it will remove data from end of
# the dictionary.

dict_f = {'name': 'Rahul', 'email': 'rahul@gmail.com', 'P': 234, 'Q': 8767}
var1 = dict_f.popitem()
print("result :", var1)
print("dict_f :", dict_f) # {'name': 'Rahul', 'email': 'rahul@gmail.com', 'P': 234}


# clear method :  clear all the data from dictionary, only empty dict will remain.
dict_f.clear()
print("dict_f :", dict_f)  # dict_f : {}

# remove variable from memory using "del"
del dict_f
# print("dict_f :", dict_f)
# NameError: name 'dict_f' is not defined


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
print("dict_2:", dict_2, id(dict_2)) # {'a': 111, 'b': 222, 'c': 333}

print("_"*50)
##############################################
# sort python dictionary
list1 = [3, 1, 6, 8, 12, 2]
# sorted function takes list as input and return the sorted value in the list
# and does not modify the original list
result = sorted(list1)
print("sorted result :", result )  # list1 = [1, 2, 3, 6, 8, 12]
print("list1 :", list1) # list1 : [3, 1, 6, 8, 12, 2]

list1.sort() # sort method modifies original list
print("list1 :", list1) # [1, 2, 3, 6, 8, 12]

print("#"*50)
#########################################################

my_dict = {'a': 500, 'c': 200, 'e': 400, 'b': 700}

# sorted with keys of dicts
sorted_dict = sorted(my_dict.items())
print(sorted_dict) # [('a', 500), ('b', 700), ('c', 200), ('e', 400)]
print(dict(sorted_dict)) # {'a': 500, 'b': 700, 'c': 200, 'e': 400}


# sorted with values of dict
result2 = sorted(my_dict.items(), key=lambda item:item[1])
print("sorted dict with values :", dict(result2))
# {'c': 200, 'e': 400, 'a': 500, 'b': 700}


print("_"*40)
nested_list = [['a', 1], ['d', 10], ['c', 30], ['e', 20]]
result3 = sorted(nested_list)
print(result3) # [['a', 1], ['c', 30], ['d', 10], ['e', 20]]

# sorted on the basic index second value of child key
result4 = sorted(nested_list, key=lambda x: x[1])
print("result4 :", result4) # [['a', 1], ['d', 10], ['e', 20], ['c', 30]]


result5 = sorted(nested_list, key=lambda x: x[1])
print("result5 :", result5) # [['a', 1], ['d', 10], ['e', 20], ['c', 30]]

print("_"*50)
######################################
list2 = [50, 20, 1, 3, 5, 7]

ascending_sort = sorted(list2)
print(ascending_sort) # [1, 3, 5, 7, 20, 50]

descending_sort = sorted(list2, reverse=True)
print(descending_sort) # [50, 20, 7, 5, 3, 1]

my_dict = {'a': 500, 'c': 200, 'e': 400, 'b': 700}


dict_desc = sorted(my_dict.items(), reverse=True)
print("descending order :", dict(dict_desc))
# {'e': 400, 'c': 200, 'b': 700, 'a': 500}

