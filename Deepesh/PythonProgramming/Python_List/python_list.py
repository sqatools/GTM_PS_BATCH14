"""
# Properties:
-> List is mutable data type, that we can modify any point of time.
-> List can contain any types of data, int, float, complex, str, list, tuple, dict, set, boolean.
-> List follows positive negative indexing as like string.
-> We define list with square bracket.
"""

list1 = [2, 3.5, 5+7j, 'Hello', [4, 6, 8], (1, 3, 5), {'a': 123, 'b': 125}, {4, 6, 7}, True]
print(list1, type(list1))
# [2, 3.5, (5+7j), 'Hello', [4, 6, 8], (1, 3, 5), {'a': 123}, {4, 6, 7}, True] <class 'list'>

# Get data from list using index
print(list1[3])  # Hello
print(list1[3][1])  # e

# get child list from given list
print(list1[4])  # [4, 6, 8]
print(list1[4][1])  # 6

print(list1[-3])  # {'a': 123, 'b': 125}
print(list1[-3]['b']) # 125


# x + yj
# x : real number
# y : img number

var = 10 + 30j
print(var, type(var))  #(10+30j) <class 'complex'>
print(var.real) # 10.0
print(var.imag) # 30.0

print("_"*50)
##################################################
# Apply loop on the list
list2 = ['a', 'b', 'c', 'd']
for p in list2:
    print(p)

print("_"*50)
for i in range(len(list2)):
    print(i, list2[i])


x = 'a'
if x in list2:
    print(x)


######################## slicing in list ######################
"""
# Rule1 : list[start index:  end index]

->  In this rule it will always get output from left to right.
->  default start index value is 0
->  default end index value is end of list.
->  start index and end index could be positive negative.
->  Output will include the start index value and exclude end index value

# Rule2 : list[start index:  end index: step value]

-> In this rule, output will include start index value and exclude end index value
-> default start index is zero (0) if step value is +ve
-> default start index is -1 if step value is -ve
-> default end index will be end of list if step value is +ve
-> default end index will be start of list if step value is -ve


"""
list3 = [4, 7, 12, 50, 70, 33, 21]
print(list3[0:4])  # [4, 7, 12, 50]
print(list3[3:7]) # [50, 70, 33, 21]
print(list3[0:7:2]) # [4, 12, 70, 21]
print(list3[-2:-6:-1]) # [33, 70, 50, 12]
print(list3[-1:-8:-1]) # [21, 33, 70, 50, 12, 7, 4]
print(list3[::-1])  # [21, 33, 70, 50, 12, 7, 4]

print("_"*50)
######################## List Methods #####################
print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

print("_"*50)
##################
# append() method :  This method add data to the list at the end of the list.
list_a = [5, 7, 9, 10, 21]
list_a.append(100)
print("list_a :", list_a)  # [5, 7, 9, 10, 21, 100]
list_a.append('Python')
print("list_a :", list_a) # [5, 7, 9, 10, 21, 100, 'Python']


print("_"*50)
##################
# insert() method : this method add data to the list at specific index position.
list_b = [6, 7, 8, 10, 30, 40]
list_b.insert(2, 100)
print("list_b :", list_b) # list_b : [6, 7, 100, 8, 10, 30, 40]


print("_"*50)
##################
# extend() method :  this method add one list data to another list
list_c = ['a', 'b']
list_d = [11, 22, 33, 44]
list_d.extend(list_c)

print("list_d :", list_d) # [11, 22, 33, 44, 'a', 'b']
print("list_c :", list_c) # ['a', 'b']

str1 = 'hello'
list_f = [1, 2, 3]
list_f.extend(str1)
print("list_f :", list_f)
# [1, 2, 3, 'h', 'e', 'l', 'l', 'o']

dict1= {'a': 123, 'b': 567}
list2 = [5, 67, 8]
list2.extend(dict1)
print("list2 :", list2) # [5, 67, 8, 'a', 'b']


print("_"*50)
##################
# remove() method:  this method remove any specific data from list
#                   -> if value is repeated multiple times, then it will remove first occurrence
list_x = [10, 20, 30, 40, 30]
list_x.remove(30)
print("list_x :", list_x)  # [10, 20, 40, 30]

print("_"*50)
##################
# pop() method :  This method remove data from specific index position and return the value.
#                 default index position is -1
list_y = ['a', 'b', 'c', 'd', 'f', 'b']

# remove from default index -1
v1 = list_y.pop()
print("removed value :", v1) # b
print("list_y :", list_y) # ['a', 'b', 'c', 'd', 'f']

# remove from specific index
v2 = list_y.pop(2)
print("removed value :", v2)  # removed value : c
print("list_y :", list_y) # ['a', 'b', 'd', 'f']








