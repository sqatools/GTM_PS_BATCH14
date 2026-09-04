"""
# Properties:
-> List is mutable data type, that we can modify any point of time.
-> List can contain any types of data, int, float, complex, str, list, tuple, dict, set, boolean.
-> List follows positive negative indexing as like string.
-> We define list with square bracket.
"""

list1 = [2, 3.5, 5 + 7j, 'Hello', [4, 6, 8], (1, 3, 5), {'a': 123, 'b': 125}, {4, 6, 7}, True]
print(list1, type(list1))
# [2, 3.5, (5+7j), 'Hello', [4, 6, 8], (1, 3, 5), {'a': 123}, {4, 6, 7}, True] <class 'list'>

# Get data from list using index
print(list1[3])  # Hello
print(list1[3][1])  # e

# get child list from given list
print(list1[4])  # [4, 6, 8]
print(list1[4][1])  # 6

print(list1[-3])  # {'a': 123, 'b': 125}
print(list1[-3]['b'])  # 125

# x + yj
# x : real number
# y : img number

var = 10 + 30j
print(var, type(var))  # (10+30j) <class 'complex'>
print(var.real)  # 10.0
print(var.imag)  # 30.0

print("_" * 50)
##################################################
# Apply loop on the list
list2 = ['a', 'b', 'c', 'd']
for p in list2:
    print(p)

print("_" * 50)
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
print(list3[3:7])  # [50, 70, 33, 21]
print(list3[0:7:2])  # [4, 12, 70, 21]
print(list3[-2:-6:-1])  # [33, 70, 50, 12]
print(list3[-1:-8:-1])  # [21, 33, 70, 50, 12, 7, 4]
print(list3[::-1])  # [21, 33, 70, 50, 12, 7, 4]

print("_" * 50)
######################## List Methods #####################
print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

print("_" * 50)
##################
# append() method :  This method add data to the list at the end of the list.
list_a = [5, 7, 9, 10, 21]
list_a.append(100)
print("list_a :", list_a)  # [5, 7, 9, 10, 21, 100]
list_a.append('Python')
print("list_a :", list_a)  # [5, 7, 9, 10, 21, 100, 'Python']

print("_" * 50)
##################
# insert() method : this method add data to the list at specific index position.
list_b = [6, 7, 8, 10, 30, 40]
list_b.insert(2, 100)
print("list_b :", list_b)  # list_b : [6, 7, 100, 8, 10, 30, 40]

print("_" * 50)
##################
# extend() method :  this method add one list data to another list
list_c = ['a', 'b']
list_d = [11, 22, 33, 44]
list_d.extend(list_c)

print("list_d :", list_d)  # [11, 22, 33, 44, 'a', 'b']
print("list_c :", list_c)  # ['a', 'b']

str1 = 'hello'
list_f = [1, 2, 3]
list_f.extend(str1)
print("list_f :", list_f)
# [1, 2, 3, 'h', 'e', 'l', 'l', 'o']

dict1 = {'a': 123, 'b': 567}
list2 = [5, 67, 8]
list2.extend(dict1)
print("list2 :", list2)  # [5, 67, 8, 'a', 'b']

print("_" * 50)
##################
# remove() method:  this method remove any specific data from list
#                   -> if value is repeated multiple times, then it will remove first occurrence
list_x = [10, 20, 30, 40, 30, 60]
list_x.remove(30)
print("list_x :", list_x)  # [10, 20, 40, 30]

list_x.remove(10)
print("list_x :", list_x)

print("_" * 50)
##################
# pop() method :  This method remove data from specific index position and return the value.
#                 default index position is -1
list_y = ['a', 'b', 'c', 'd', 'f', 'b']

# remove from default index -1
v1 = list_y.pop()
print("removed value :", v1)  # b
print("list_y :", list_y)  # ['a', 'b', 'c', 'd', 'f']

# remove from specific index
v2 = list_y.pop(2)
print("removed value :", v2)  # removed value : c
print("list_y :", list_y)  # ['a', 'b', 'd', 'f']

print("_" * 50)
################################
# sort() method : This method sort list data in ascending and d-escending order.
#                 This method will update the original list

list_1 = [6, 2, 7, 1, 3, 5]
list_1.sort()
print("Ascending order list :", list_1)
# [1, 2, 3, 5, 6, 7]

list_2 = [6, 2, 17, 1, 3, 5, 10, 11]
list_2.sort(reverse=True)
print("Descending order list :", list_2)
# [17, 11, 10, 6, 5, 3, 2, 1]

list_a = ['Hello', 'we', 'are', 'learning', 'Python', 'Polo']
list_a.sort()
print("list_a :", list_a)  # ['Hello', 'Polo', 'Python', 'are', 'learning', 'we']

print("#" * 50)
################################
# reverse() method : This method reverse list data and modify the original list.

list_3 = [6, 2, 7, 1, 3, 5, 20, 30]
list_3.reverse()
print("list_3 :", list_3)  # [30, 20, 5, 3, 1, 7, 2, 6]

print("#" * 50)
################################
# count() method : This method count the number of occurrences of any given value

list_4 = [6, 12, 7, 1, 3, 5, 20, 12, 30, 7, 12]
print("count of 12 :", list_4.count(12))  # count of 12 : 3

print("#" * 50)
################################
# index() method : This method return the index of given value

list_5 = [6, 12, 7, 10, 300, 500, 20, 12, 30, 7, 12]
print("index of 500 :", list_5.index(500))  # index of 500 : 5

print("#" * 50)
################################
# clear() method : This method clear all data from list and remain empty list.

list_6 = [6, 12, 7, 10, 300, 500, 20, 12, 30, 7, 12]
list_6.clear()

print("list_6 :", list_6)  # list_6 : []

print("#" * 50)
############################################################
# list concatenation :  combine two list data with plus operation without changing the original list

list_a = ['a', 'b', 'c']
list_b = [10, 20, 30]
list_c = list_a + list_b
print("list_c :", list_c)  # ['a', 'b', 'c', 10, 20, 30]

# list repetition :  when we multiply list with any number, then it will repeat the list values that numbers of
# time.

list_x = [2, 5, 7]
print(list_x * 5)  # [2, 5, 7, 2, 5, 7, 2, 5, 7, 2, 5, 7, 2, 5, 7]

print("#" * 50)
############### Max, Min, sum #############

list_y = [50, 60, 30, 12, 16]
print("Max value:", max(list_y))  # Max value: 60
print("Min value :", min(list_y))  # Min value : 12
print("Sum of values :", sum(list_y))  # Sum of values : 168

list_z = ['abc', 'hello', 'Python', 'Programming']
print(max(list_z))

# ASCII VALUES
# A-Z : 65- 90
# a -z : 97 - 122

for i in range(65, 91):
    print(chr(i), end=" ")
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
print()

for j in range(97, 123):
    print(chr(j), end=" ")

# a b c d e f g h i j k l m n o p q r s t u v w x y z

print("_" * 50)
# ord() function :  this function return ASCII of value of character
print("ASCII of a:", ord('a'))  # ASCII of a: 97

print("_"*50)
###################################################################
# Q1 : write a python program to get all even values from list
list1 = [4, 5, 7, 8, 12, 17, 56]
#output = [4, 8, 12, 56]

output = []

for val in list1:
    print(output)
    if val%2 == 0:
        output.append(val)
    else:
        continue

print("Output :", output) # [4, 8, 12, 56]

print("_"*50)
# solution with List comprehension
result = [x for x in list1 if x%2 == 0]
print("result :", result) # [4, 8, 12, 56]

print("_"*50)
########################################################
# Q2 : write a python program to get all even and odd values with tag from list
list1 = [4, 5, 7, 8, 12]
# result = [(4, 'even'), (5, 'odd'), (7, 'odd'), (8, 'even'), (12, 'even')]

result = []
for val in list1:
    if val%2  == 0:
        result.append((val, 'even'))
    else:
        result.append((val, 'odd'))

print("result :", result)

print("-"*50)
# solve same program with list comprehension
result2 = [(y, 'even') if y%2 == 0 else (y, 'odd') for y in list1]
print("result2 :", result2)


print("_"*50)
# get square of all value
list_2 = [5, 7, 8, 2, 9]
square = [x**2 for x in list_2]
print("square of values :", square)
# [25, 49, 64, 4, 81]