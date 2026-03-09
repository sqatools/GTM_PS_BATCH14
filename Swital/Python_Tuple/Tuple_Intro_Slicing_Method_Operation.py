"""
# Properties:
-> Tuple is immutable data type, that we can not modify.
-> Tuple can contain any types of data, int, float, complex, str, list, tuple, dict, set, boolean.
-> Tuple follows positive negative indexing as like list and string.
-> We can define tuple with round bracket. e.g. tup1 = (4, 6, 8)
"""

tup1 = (1, 2.3, 'Hello', (4, 6, 7), [2, 4, 6], {'a': 123}, {6, 7, 8}, True)
print(tup1, type(tup1))
# (1, 2.3, 'Hello', (4, 6, 7), [2, 4, 6], {'a': 123}, {8, 6, 7}, True) <class 'tuple'>

# get value from tuple using indexing
print(tup1[5])  # {'a': 123}

# get partial value using slicing
print(tup1[3:6])  # ((4, 6, 7), [2, 4, 6], {'a': 123})
print(tup1[::-1])  # (True, {8, 6, 7}, {'a': 123}, [2, 4, 6], (4, 6, 7), 'Hello', 2.3, 1)

print("_" * 50)
################################
tup2 = (10, 20, 30, 50)
for val in tup2:
    print(val)

"""
10
20
30
50
"""

print("_" * 50)
################# Methods for tuple ##############
print(dir(tuple))  # 'count', 'index'

tup3 = ('a', 'b', 'c', 'a', 'd', 4, 5, 7, 12)
print("count of a :", tup3.count('a'))  # count of a : 2
print("index of 4 :", tup3.index(4))  # index of 4 : 5

print("#" * 50)
tup4 = (4, 7, 309, 20, 12, 15)
print("tuple repitation :", tup4 * 2)
# (4, 7, 309, 20, 12, 15, 4, 7, 309, 20, 12, 15)

# concatenation
tup5 = tup4 + (15, 16, 17)
print(tup5)  # (4, 7, 309, 20, 12, 15, 15, 16, 17)

##############################################
print("#" * 50)
tup6 = (4, 7, 309, 20, 12, 15)
print("Max values :", max(tup6))  # Max values : 309
print("Min values :", min(tup6))  # Min values : 4
print("Sum of values :", sum(tup6))  # Sum of values : 367

print("#"*50)
############################################
# program to get combination of number whose sum is 10
tup6 = (5, 7, 8, 2, 3, 1, 9)
#output = [(7, 3), (8, 2), (1, 9)]
output = [] # empty

for i in range(len(tup6)): # i = 0
    for j in range(i+1, len(tup6)): # j (1, 7)
        if tup6[i] + tup6[j] == 10:
            output.append((tup6[i], tup6[j]))
        else:
            continue

print("Output :", output)  # Output : [(7, 3), (8, 2), (1, 9)]

###########################################
# write a python program to create a dictionary with zip function using 2 lists
l1 = ['a', 'b', 'c', 'd']
l2 = [123, 456, 789]

result = dict(zip(l1, l2))
print("result :", result)
# {'a': 123, 'b': 456, 'c': 789}

r1 = zip(l1, l2)
print("r1:", list(r1))  # [('a', 123), ('b', 456), ('c', 789)]


print("_"*50)
#####################################
# tuple comprehension
tup1 = (4, 6, 8, 9, 2, 3)
result = tuple(x**2 for x in tup1)
print("result:", result)  # (16, 36, 64, 81, 4, 9)

# get all even value from tuple
result2 = tuple(x for x in tup1 if x%2 ==0)
print("result2 :", result2) # (4, 6, 8, 2)