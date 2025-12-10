print(dir(list))
'''
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
'__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', 
'__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
'__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 
'reverse', 'sort']

'''
print()
# ************* Append Method ***************
print('-' * 15, 'Append Method', '-' * 15)
l1 = [1, 33, 24, 100, 22]
print(l1)
l1.append(67)
print('new:', l1)  # [1, 33, 24, 100, 22, 67]

print()
# ************* Insert Method ***************
print('-' * 15, 'Insert Method', '-' * 15)
l1 = [1, 33, 24, 100, 22]
print(l1)
l1.insert(2, 31)
print('New', l1)  # New [1, 33, 31, 24, 100, 22]

l1.insert(-2, 40) # will insert data after the negative index data
print('neg new', l1)  # neg new [1, 33, 31, 24, 40, 100, 22]

print()
# ************* Extend Method ***************
print('-' * 15, 'Extend Method', '-' * 15)
l1 = [1, 33, 24, 100, 22]
l2 = ['a', 'b']
l1.extend(l2)
print(l1)  # [1, 33, 24, 100, 22, 'a', 'b']
print(l2)  # ['a', 'b']

s1 = [1, 2]
s2 = 'hi'
s3 = s1.extend(s2) #NA
print(s1)  # [1, 2, 'h', 'i']
print(s2)  # hi
print(s3)  # None

print()
# ************* Remove Method ***************
print('-' * 15, 'Remove Method', '-' * 15)
l1 = [1, 33, 24, 100, 22]
l1.remove(100)
print(l1) # [1, 33, 24, 22]
l2=[1,2,3,2,5]
l2.remove(2)
print(l2) # [1, 3, 2, 5]

print()
# ************* Pop Method ***************
print('-' * 15, 'Pop Method', '-' * 15)
l1 = [1, 33, 24, 100, 22]
s1= l1.pop()
print('Default value removed is from -1:', s1) # Default value removed is from -1: 22
print(l1) # [1, 33, 24, 100]
s2=l1.pop(-2)
print(s2) # 24


