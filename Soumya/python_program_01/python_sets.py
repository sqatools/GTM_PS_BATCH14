"""
# Properties:
-> Set is mutable data type, we can modify it at any point of time.
-> Set store value in curly bracket, {}
-> Set only allows immutable type as member, int, float, complex, string, tuple, boolean.
-> Set only contains unique values, duplicate values are not allowed.
-> Set store values in random order.
-> Set does not follow indexing.
"""
set1 = {12, 3.5, 'Python', (3, 5, 6), True, 12, 3.5}
print(set1, type(set1))
# {'Python', True, 3.5, (3, 5, 6), 12} <class 'set'>

####Set methods #######
print(dir(set1))
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

print("_" * 50)
############
# add() method : This method add data to the set in random order.
set2 = {5, 7, 9, 20, 10}
set2.add(30)
print("set2 :", set2)  # {20, 5, 7, 9, 10, 30}

print("_" * 50)
############
# update() method : This method update one set data to another set.
set3 = {5, 7, 9, 20, 10}
set4 = {'a', 'b', 'c'}
set3.update(set4)
print("set3 :", set3)  # {'c', 20, 5, 'a', 7, 'b', 9, 10}
print("set4 :", set4)  # {'c', 'a', 'b'}

print("_" * 50)
############
# union() method : This method combine two sets data and generate new set as output.
set13 = {5, 7, 9, 20, 10}
set14 = {'a', 'b', 'c'}
set15 = set13.union(set14)
print("set15 :", set15)  # {20, 5, 'b', 7, 9, 10, 'c', 'a'}

print("_" * 50)
############
# remove() method : This method remove any specific from set. it does not return anything
set6 = {5, 7, 9, 20, 10, 11, 25}
set6.remove(10)
print("set6 :", set6)  # {20, 5, 7, 9, 11, 25}

# remove non existing value
# set6.remove(30)  # KeyError: 30
print("set6 :", set6)

print("_" * 50)
############
# discard() method : This method remove any specific from set. it does not return anything
# if target value is not available then it will not throw any error
set7 = {15, 17, 9, 20, 10, 11, 25}
set7.discard(17)
print("set7 :", set7)  # {20, 9, 10, 11, 25, 15}

# discard non existing value
set7.discard(50)  # if target value is not there is will not throw any error.
print("set7 :", set7)  # {20, 9, 10, 11, 25, 15}

print("_" * 50)
############
# difference() method : this method provide the difference of value from one set to another.
set8 = {5, 7, 9, 20}
set9 = {'a', 'b', 5, 7}

result = set8.difference(set9)
print("difference between 2 sets", result)  # {9, 20}

print("_" * 50)
############
# intersection() method : this method provide the common values between 2 sets.
set10 = {5, 7, 9, 20}
set11 = {'a', 'b', 5, 7}
result3 = set10.intersection(set11)
print("Result3 :", result3)  # {5, 7}

print("_" * 50)
############
# symmetric_difference() method : this method provide the difference of values in both sets
set13 = {5, 7, 9, 20}
set14 = {'a', 'b', 5, 7}

result13 = set13.symmetric_difference(set14)
print("symmetric difference :", result13)  # {9, 'a', 'b', 20}

######### copy method #############
# shallow copy : this method use shallow copy concept when we assign one set to another set and modify value in
# any of the set, then changes will reflect in both sets.

s1 = {'a', 'b', 'c', 'd'}
s2 = s1
s2.add(10)
s1.add(100)
print("s1 set :", s1)  # {100, 'a', 10, 'b', 'c', 'd'}
print("s2 set :", s2)  # {100, 'a', 10, 'b', 'c', 'd'}


print("#"*50)
##################################################
# Deep copy:  In the concept we will use copy method explicitly and does if we modify the any of the set, then
# changes will reflect in that dedicated set only.

set_a = {'a', 'b', 'c', 'd'}
set_b = set_a.copy()
set_b.add(100) # {200, 'a', 'd', 'b', 'c'}
set_a.add(200)
print("set_a :", set_a) # {200, 'a', 'd', 'b', 'c'}
print("set_b :", set_b) # {100, 'a', 'd', 'b', 'c'}

print("_"*50)
###################################################
# pop method :  this method remove value from set and return it.
set_c = {200, 'a', 'd', 'b', 'c'}
val = set_c.pop()
print("removed value :", val) #  a
print("updated set :", set_c)  # {'b', 200, 'd', 'c'}


print("_"*50)
###################################################
# clear() method: This method clear all the data from set and remain only empty set.
set_d = {5, 7, 9, 2, 0, 12}
set_d.clear()
print("set_d :", set_d) # set_d : set()

a = {} # empty dict
b = set() # empty set

print("_"*50)
#############################
# Apply loop on set
set_d = {5, 7, 9, 2, 12}
for val in set_d:
    print(val)

"""
2
5
7
9
12
"""
print("_"*50)
###################### frozenset #########
# frozenset, freeze all values of set, once it is defined we can not do any modification on set.
list1 = [6, 8, 3, 3, 6, 12, 12, 34]
list1.append(50)

frozen_set = frozenset(list1)
print("frozen set :", frozen_set, type(frozen_set))
#frozen_set.add(100) # AttributeError: 'frozenset' object has no attribute 'add'
list1.append(200)

list2 = ['a', 'b', 'c', 'd']
fset2 = frozenset(list2)

result = frozen_set.union(fset2)
print(" result:", result) # frozenset({34, 3, 6, 8, 'c', 12, 'b', 50, 'a', 'd'})

print("_"*50)
###################################
#program : get all the even values from set.

set3 = {3, 5, 7, 8, 9, 10, 11}
set5 = set()

for val in set3:
    if val%2 == 0:
        set5.add(val)
    else:
        continue

print("set output :", set5)  # {8, 10}

# HW1 :  write a python program to get all the values which are divisible by 3 and 5 from set.

print("_"*50)
####################################
#Q1 move data from one set to another.
"""
# Properties:
-> Set is mutable data type, we can modify it at any point of time.
-> Set store value in curly bracket, {}
-> Set only allows immutable type as member, int, float, complex, string, tuple, boolean.
-> Set only contains unique values, duplicate values are not allowed.
-> Set store values in random order.
-> Set does not follow indexing.
"""
set1 = {12, 3.5, 'Python', (3, 5, 6), True, 12, 3.5}
print(set1, type(set1))
# {'Python', True, 3.5, (3, 5, 6), 12} <class 'set'>

####Set methods #######
print(dir(set1))
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

print("_" * 50)
############
# add() method : This method add data to the set in random order.
set2 = {5, 7, 9, 20, 10}
set2.add(30)
print("set2 :", set2)  # {20, 5, 7, 9, 10, 30}

print("_" * 50)
############
# update() method : This method update one set data to another set.
set3 = {5, 7, 9, 20, 10}
set4 = {'a', 'b', 'c'}
set3.update(set4)
print("set3 :", set3)  # {'c', 20, 5, 'a', 7, 'b', 9, 10}
print("set4 :", set4)  # {'c', 'a', 'b'}

print("_" * 50)
############
# union() method : This method combine two sets data and generate new set as output.
set13 = {5, 7, 9, 20, 10}
set14 = {'a', 'b', 'c'}
set15 = set13.union(set14)
print("set15 :", set15)  # {20, 5, 'b', 7, 9, 10, 'c', 'a'}

print("_" * 50)
############
# remove() method : This method remove any specific from set. it does not return anything
set6 = {5, 7, 9, 20, 10, 11, 25}
set6.remove(10)
print("set6 :", set6)  # {20, 5, 7, 9, 11, 25}

# remove non existing value
# set6.remove(30)  # KeyError: 30
print("set6 :", set6)

print("_" * 50)
############
# discard() method : This method remove any specific from set. it does not return anything
# if target value is not available then it will not throw any error
set7 = {15, 17, 9, 20, 10, 11, 25}
set7.discard(17)
print("set7 :", set7)  # {20, 9, 10, 11, 25, 15}

# discard non existing value
set7.discard(50)  # if target value is not there is will not throw any error.
print("set7 :", set7)  # {20, 9, 10, 11, 25, 15}

print("_" * 50)
############
# difference() method : this method provide the difference of value from one set to another.
set8 = {5, 7, 9, 20}
set9 = {'a', 'b', 5, 7}

result = set8.difference(set9)
print("difference between 2 sets", result)  # {9, 20}

print("_" * 50)
############
# intersection() method : this method provide the common values between 2 sets.
set10 = {5, 7, 9, 20}
set11 = {'a', 'b', 5, 7}
result3 = set10.intersection(set11)
print("Result3 :", result3)  # {5, 7}

print("_" * 50)
############
# symmetric_difference() method : this method provide the difference of values in both sets
set13 = {5, 7, 9, 20}
set14 = {'a', 'b', 5, 7}

result13 = set13.symmetric_difference(set14)
print("symmetric difference :", result13)  # {9, 'a', 'b', 20}

######### copy method #############
# shallow copy : this method use shallow copy concept when we assign one set to another set and modify value in
# any of the set, then changes will reflect in both sets.

s1 = {'a', 'b', 'c', 'd'}
s2 = s1
s2.add(10)
s1.add(100)
print("s1 set :", s1)  # {100, 'a', 10, 'b', 'c', 'd'}
print("s2 set :", s2)  # {100, 'a', 10, 'b', 'c', 'd'}


print("#"*50)
##################################################
# Deep copy:  In the concept we will use copy method explicitly and does if we modify the any of the set, then
# changes will reflect in that dedicated set only.

set_a = {'a', 'b', 'c', 'd'}
set_b = set_a.copy()
set_b.add(100) # {200, 'a', 'd', 'b', 'c'}
set_a.add(200)
print("set_a :", set_a) # {200, 'a', 'd', 'b', 'c'}
print("set_b :", set_b) # {100, 'a', 'd', 'b', 'c'}

print("_"*50)
###################################################
# pop method :  this method remove value from set and return it.
set_c = {200, 'a', 'd', 'b', 'c'}
val = set_c.pop()
print("removed value :", val) #  a
print("updated set :", set_c)  # {'b', 200, 'd', 'c'}


print("_"*50)
###################################################
# clear() method: This method clear all the data from set and remain only empty set.
set_d = {5, 7, 9, 2, 0, 12}
set_d.clear()
print("set_d :", set_d) # set_d : set()

a = {} # empty dict
b = set() # empty set

print("_"*50)
#############################
# Apply loop on set
set_d = {5, 7, 9, 2, 12}
for val in set_d:
    print(val)

"""
2
5
7
9
12
"""
print("_"*50)
###################### frozenset #########
# frozenset, freeze all values of set, once it is defined we can not do any modification on set.
list1 = [6, 8, 3, 3, 6, 12, 12, 34]
list1.append(50)

frozen_set = frozenset(list1)
print("frozen set :", frozen_set, type(frozen_set))
#frozen_set.add(100) # AttributeError: 'frozenset' object has no attribute 'add'
list1.append(200)

list2 = ['a', 'b', 'c', 'd']
fset2 = frozenset(list2)

result = frozen_set.union(fset2)
print(" result:", result) # frozenset({34, 3, 6, 8, 'c', 12, 'b', 50, 'a', 'd'})

print("_"*50)
###################################
#program : get all the even values from set.

set3 = {3, 5, 7, 8, 9, 10, 11}
set5 = set()

for val in set3:
    if val%2 == 0:
        set5.add(val)
    else:
        continue

print("set output :", set5)  # {8, 10}

# HW1 :  write a python program to get all the values which are divisible by 3 and 5 from set.

print("*"*50)
set11 = {6, 7, 8, 3, 16, 12}
for val in set11:
    if val%3 == 0 and val%5==0:
        print("all the values which are divisible by 3 and 5 are:", val)


print("_"*50)
####################################
#Q1 move data from one set to another.
set_x = {6, 7, 8, 3, 16, 12}
set_y = set()

#output :
#set_x = set()
#set_y = {6, 7, 8, 3, 16, 12}


for i in range(len(set_x)):
    val = set_x.pop()
    set_y.add(val)


print("set_x :", set_x) # set_x : set()
print("set_y :", set_y) # set_y : {3, 6, 7, 8, 12, 16}

set_y = set()

#output :
#set_x = set()
#set_y = {6, 7, 8, 3, 16, 12}


for i in range(len(set_x)):
    val = set_x.pop()
    set_y.add(val)


print("set_x :", set_x) # set_x : set()
print("set_y :", set_y) # set_y : {3, 6, 7, 8, 12, 16}