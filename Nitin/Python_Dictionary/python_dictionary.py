print("Hi")
# immutable data type
# int,str,tuple,bolean
'''
dict={'a':123
       1:222
       (2,3,4):4444
       True:0}
'''
dict={'a':123,
       1:222,
       (2,3,4):4444,
       True: {'b':0,'c':1},
      }
print(dict,type(dict))

#######################
print("-----"*11)
# apply loop on dict
dict1={'a':123,'b':222,'c':33}

for k in dict1: #a
    print(k,'the value of i')

#######################
print("-----"*11)
for k,y in dict1.items():
    print('Key:',k,'value:',y)
'''
Key: a value: 123
Key: b value: 222
Key: c value: 33
'''

#######################
print("-----"*11)
print(dir(dict))

'''
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
'''

#######################
print("-----"*11)
#### Add data to dict ####
dict3={'a':123,'b':345,'c':678}
dict3['d']:999
print(dict3)

#######################
print("-----"*11)
dict_b = {'P': 234, 'Q': 8767}
dict_c = {'name': 'Rahul', 'age': 25, 'email': 'rahul@gmail.com'}
dict_b.update(dict_c)
print(dict_b)

#######################
print("-----"*11)
# keys(), values():  These methods return list of keys and values.
dict_b = {'P': 234, 'Q': 8767}
print(dict_b.keys(),type(dict_b.keys()))
print(dict_b.keys())


#######################
print("-----"*11)
# pop():  this method remove any specific data from dict with the help of keys
dict_d = {'name': 'Rahul', 'age': 25, 'email': 'rahul@gmail.com','s':'M'}
print(dict_d.pop('s'))
print(dict_d)

#######################
print("-----"*11)
# popitem(): this method will remove key value pair from dict and return it. it will remove data from end of

#updatinf the dictionary
dict_d['Roll']=1201
print(dict_d)
print(dict_d.popitem())
#print(dict_d)
print(dict_d.values())
print(dict_d.items())

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

dict_n={'name':'Nitin','Age': 30}
#dict_k={'Area':'S.D.O'}
dict_k=dict_n
print(dict_n)
print(dict_k)
dict_k['Roll No']=1201
print(dict_n,id(dict_n))
print(dict_k,id(dict_k))


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

