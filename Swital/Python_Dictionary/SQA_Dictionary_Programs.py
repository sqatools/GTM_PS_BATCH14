# 1). Python Dictionary program to add elements to the dictionary.
dictionary = {"name": "swital", "age" : 25, "profession" : "QA"}
print(dictionary)

dictionary1 = {}
dictionary1["language"] = "python"
dictionary1["data"] = "3"
print(dictionary1)

# 2). Python Dictionary program to print the square of all values in a dictionary.
"""Input : {‘a’: 5, ‘b’:3, ‘c’: 6, ‘d’ : 8}
Output :
a : 25
b : 9
c : 36
d : 64"""
d2 = {'a': 5, 'b':3, 'c': 6, 'd' : 8}

for value in d2:
    print(value, ":", d2[value]**2)

#3). Python Dictionary program to move items from dict1 to dict2.
"""Input :
dict1 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
dict2 = {}
Output :
dict1 = {}
dict2 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}"""
dict1 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
dict2 = {}
temp = dict1.copy()
for val in temp:
    dict2[val] = dict1.pop(val)
print(dict1)
print(dict2)

# 4). Python Dictionary program to concatenate two dictionaries.
"""Input :
dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’}
dict2 = {‘Age’ : 25, ‘salary’: ‘$25k’}
Output :
dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’, ‘Age’ : 25, ‘salary’: ‘$25k’}"""
dict1 = {'Name': 'Harry', 'Rollno': 345, 'Address': 'Jordan'}
dict2 = {'Age': 25, 'salary': '$25k'}
dict1.update(dict2)
print(dict1)

# 5). Python Dictionary program to get a list of odd and even keys from the dictionary.
"""Input :
{1: 25, 5:’abc’, 8:’pqr’, 21:’xyz’, 12:’def’, 2:’utv’}
Output :
Even Key = [[8, ‘pqr’], [12, ‘def’], [2, ‘utv’]]
Odd Key = [[1, 25], [5, ‘abc’], [21, ‘xyz’]]"""

d5 = {1: 25, 5: 'abc', 8: 'pqr', 21: 'xyz', 12: 'def', 2: 'utv'}
even_key = []
odd_key = []
for val in d5:
    if val%2 ==0:
        even_key.append([val,d5[val]])
    else:
        odd_key.append([val, d5[val]])
print("Even Key:", even_key)
print("Odd Key:", odd_key)

# 6). Python Dictionary Program to create a dictionary from two lists.
"""Input :
list1 = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’]|
list2 = [12, 23, 24, 25, 15, 16]
Output :
{‘a’: 12, ‘b’: 23, ‘c’: 24, ‘d’: 25, ‘e’: 15}"""

list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [12, 23, 24, 25, 15, 16]

dict1 = {}
for a,b in zip(list1, list2):
    dict1[a] = b
print(dict1)

# 7). Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
"""Input :
[4, 5, 6, 2, 1, 7, 11]
Output :
{4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}""" 

d7 = [4, 5, 6, 2, 1, 7, 11]
dict1 = {}
for val in d7:
    if val %2 == 0:
        dict1[val] = val**2
    else:
        dict1[val] = val**3
print(dict1)

# 8). Python Dictionary program to clear all items from the dictionary.
dict1 = {1: 25, 5: 'abc', 8: 'pqr', 21: 'xyz', 12: 'def', 2: 'utv'}
dict1.clear()
print(dict1)

# 9). Python Dictionary program to remove duplicate values from Dictionary.
"""Input :
{‘a’: 12, ‘b’: 2, ‘c’: 12, ‘d’: 5, ‘e’: 35, ‘f’: 5}
Output :
{‘a’: 12, ‘b’: 2, ‘d’: 5, ‘e’: 35}"""
dict1 = {'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}
dict2 = {}
for key,val in dict1.items():
    if key not in dict2.values():
        dict2[key] = val
print(dict2)

#10). Python Dictionary program to create a dictionary from the string.
#Input  = ‘SQATools’
#Output = {‘S’: 1, ‘Q’: 1, ‘A’: 1, ‘T’: 1, ‘o’: 2, ‘l’: 1, ‘s’: 1}

string = "SQATools"
dict2 = {}
for ch in string:
    dict2[ch] = string.count(ch)
print(dict2)


