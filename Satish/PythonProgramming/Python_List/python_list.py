print(dir(list))

#List methods
"""
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""

list_a=[10,11,12,13,14]
list_a.append(30)
print(list_a)
list_a.insert(1,50)
print(list_a)
list_b=['a','b','c','d']

print("_"*50)
list_c=[11,12,13,14,15]
list_c.extend(list_b)
print(list_c)

print("_"*50)
list_d=[10,20,30,40,50]
list_d.remove(50)
print(list_d)

list_e=[11,22,33,44,55]
list_e.pop()
print(list_e)

list_f=[30,31,32,33,34,35]
list_f.pop(1)
print(list_f)

