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

print()
# ************* sort Method ***************
print('-' * 15, 'Sort Method', '-' * 15)
l1=[33,2,4,12,0,34]
l1.sort()
print("value in ascending order: ", l1) # value in ascending order:  [0, 2, 4, 12, 33, 34]

l2=[33,2,4,12,0,34]
l2.sort(reverse=True)
print("value in descending order: ", l2) # value in descending order:  [34, 33, 12, 4, 2, 0]

l3=['Are','python','Program','clock']
l3.sort()
print("Ascending order :", l3) # Ascending order : ['Are', 'Program', 'clock', 'python']

l4=['Hello','Python','ant','we']
l4.sort(reverse=True)
print("Descending order:", l4) # Descending order: ['we', 'ant', 'Python', 'Hello']

'''
l5=['Check',2,55,'april',34]
l5.sort(reverse=True)
print("Ascending alphanumeric:", l5) # no output for ascending and descending
'''

print()
# ************* Reverse Method ***************
print('-' * 15, 'Reverse Method', '-' * 15)
l1=[3,44,2,53,36,123]
l1.reverse()
print("Reversed number list is:",l1) # Reversed number list is: [123, 36, 53, 2, 44, 3]

l2=['Are','python','Program','clock']
l2.reverse()
print("Reversed alphabet list is:",l2) # Reversed alphabet list is: ['clock', 'Program', 'python', 'Are']

print()
# ************* Count Method ***************
print('-' * 15, 'Count Method', '-' * 15)
l1=[1,2,33,2,456,2,55,2]
r1=l1.count(2)
print("Counting total 12 by storing in var:",r1) # Counting total 12 by storing in var: 4
print("count of 12 directly:", l1.count(2)) # count of 12 directly: 4
'''
r1=l1.count(l1,33)
print(r1) #blank screen
'''
l2= ['Are','clock','python','Clock','Program','clock']
print('Var count:', l2.count('clock')) # Var count: 2
print('Capital Var count:', l2.count('Clock')) # Capital Var count: 1
print('single char count:', l2.count('y')) # single char count: 0

print()
# ************* Index Method ***************
print('-' * 15, 'Index Method', '-' * 15)
l1=[4,2,44,'clock',2,'Python']
r1=l1.index(2)
print('Index value by storing in var:', r1) # Index value by storing in var: 1
print('Index value directly',l1.index('Python')) # Index value directly 5

print()
# ************* clear Method ***************
print('-' * 15, 'clear Method', '-' * 15)
l1=[4,2,44,'clock',2,'Python']
print("Cleared list:", l1.clear()) # Cleared list: None

print()
# ************* Lisr concatenation Method ***************
print('-' * 15, 'concatenation Method', '-' * 15)
l1=[1,2,3]
l2=['are',44,'Python',2]
l3=l1+l2
print(l3) # [1, 2, 3, 'are', 44, 'Python', 2]
print(l1) # [1, 2, 3]
print(l2) # ['are', 44, 'Python', 2]

print()
# ************* List repetition  ***************
print('-' * 15, 'repetition Method', '-' * 15)
l1=[1,2,3]
l3= l1*2
print(l3) # [1, 2, 3, 1, 2, 3]

l4=[1,33,'python',4,'we']
print(l4*2) # [1, 33, 'python', 4, 'we', 1, 33, 'python', 4, 'we']

print()
# ************* Max, Min, Sum  ***************
print('-' * 15, ' Max, Min, Sum Function', '-' * 15)
l1=[22,33,4,564,234,2]
print("Max value:", max(l1)) # Max value: 564
print("Min value:", min(l1)) # Min value: 2
print("Sum total:", sum(l1)) # Sum total: 859

print('-'*20)
l2=['Python','are','We','April']
print("Max value:", max(l2)) # Max value: are
print("Min value:", min(l2)) # Min value: April
#print("Sum total:", sum(l2)) # Empty screen

print()
for i in range(65, 91):
    print(chr(i), end=" ")
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
print()

for j in range(97, 123):
    print(chr(j), end=" ")

# a b c d e f g h i j k l m n o p q r s t u v w x y z

print()
# *************ord function  ***************
print('-' * 15, ' ord Function', '-' * 15)

# ord() function :  this function return ASCII of value of character
print("ASCII of a:", ord('a'))  # ASCII of a: 97
