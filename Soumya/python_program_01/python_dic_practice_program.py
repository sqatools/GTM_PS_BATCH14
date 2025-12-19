#1). Python Dictionary program to add elements to the dictionary.

dict={}
dict["name"]="soumya"
dict["age"]=19
print(dict)

#2) Python Dictionary program to print the square of all values in a dictionary.

print("_"*50)
Input = {'a':5, 'b':6, 'c':7, 'd':8}
for val in Input:
    print(val,":",Input[val]**2)


#3). Python Dictionary program to move items from dict1 to dict2.

"""
Input :
dict1 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
dict2 = {}
Output :
dict1 = {}
dict2 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
"""
print("_"*50)
dict1 = {'name':'john', 'city': 'london', 'country': 'UK'}
dict2 = {}
temp = dict1.copy()
for val in temp:
    v1=dict1.pop(val)
    dict2[val]=v1
print(dict1)
print(dict2)


#4). Python Dictionary program to concatenate two dictionaries.
"""
Input :
dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’}
dict2 = {‘Age’ : 25, ‘salary’: ‘$25k’}
Output :
dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’, ‘Age’ : 25, ‘salary’: ‘$25k’}
"""

print("_"*50)
dict1 = {'Name': 'Harry', 'Rollno': 345, 'Address': 'Jordan'}
dict2 = {'Age': 25, 'Salary': '$25k'}
dict1.update(dict2)
print(dict1)


#5). Python Dictionary program to get a list of odd and even keys from the dictionary.

"""
Input :
{1: 25, 5:’abc’, 8:’pqr’, 21:’xyz’, 12:’def’, 2:’utv’}
Output :
Even Key = [[8, ‘pqr’], [12, ‘def’], [2, ‘utv’]]
Odd Key = [[1, 25], [5, ‘abc’], [21, ‘xyz’]]
"""

print("_"*50)
dic1={1:25, 5:'abc', 8:'pqr', 21:'xyz', 12:'def', 2:'utv'}
list1=[[val, dic1[val]] for val in dic1 if val%2==0]
list2=[[val, dic1[val]] for val in dic1 if val%2!=0]
print("even key =",list1)
print("odd key =", list2)

#6). Python Dictionary Program to create a dictionary from two lists.

"""
Input :
list1 = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’]|
list2 = [12, 23, 24, 25, 15, 16]
Output :
{‘a’: 12, ‘b’: 23, ‘c’: 24, ‘d’: 25, ‘e’: 15}

"""

print("_"*50)
list1= ['a', 'b', 'c', 'd', 'e']
list2= [12, 23, 24, 25, 15, 16]
dict1 = {}
for val1, val2 in zip(list1, list2):
    dict1[val1] = val2
print(dict1)


#7). Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
"""
Input :
[4, 5, 6, 2, 1, 7, 11]
Output :
{4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}

"""

print("_"*50)
input = {4, 5, 6, 2, 1, 7, 11}
dir1= {}
for val in input:
    if val%2==0:
        dir1[val]=val**2
    else:
        dir1[val]=val**3

print(dir1)

#8). Python Dictionary program to clear all items from the dictionary.

print("_"*50)
input = {4, 5, 6, 2, 1, 7, 11}
input.clear()
print(input)


#9). Python Dictionary program to remove duplicate values from Dictionary.

"""
Input :
{‘a’: 12, ‘b’: 2, ‘c’: 12, ‘d’: 5, ‘e’: 35, ‘f’: 5}
Output :
{‘a’: 12, ‘b’: 2, ‘d’: 5, ‘e’: 35}

"""

print("_"*50)
dict12 ={'a':12, 'b':2, 'c':12, 'd':5, 'e':35, 'f':5}
dict13={}
for key, val in dict12.items():
    if val not in dict13.values():
        dict13[key]=val
print(dict13)

#10). Python Dictionary program to create a dictionary from the string.

"""
Input  = ‘SQATools’
Output = {‘S’: 1, ‘Q’: 1, ‘A’: 1, ‘T’: 1, ‘o’: 2, ‘l’: 1, ‘s’: 1}

"""
print("_"*50)
str1='SQATools'
dir={}
for ch in str1:
    dir[ch]=str1.count(ch)
print(dir)

#11). Python Dictionary program to sort a dictionary using keys.

"""
Input = {‘d’ : 21, ‘b’ : 53,  ‘a’: 13, ‘c’: 41}
Output =
(‘a’, 13)
(‘b’, 53)
(‘c’, 41)
(‘d’, 21)

"""

print("_"*50)
dir1 = {'d': 21,'b':53, 'a':13, 'c':41}
sorted_item=sorted(dir1.items())
for key in sorted_item:
    print(key)


#12). Python Dictionary program to sort a dictionary in python using values.
"""
Input = {‘d’ : 14, ‘b’ : 52,  ‘a’: 13, ‘c’: 1 }
Output= (c, 1) (a,13) (d, 14) (b, 52)

"""
print("_"*50)
data={'d':14, 'b':52, 'a':13, 'c':1}
sorted_data = sorted(data.items(), key=lambda item: item[1])
for item in sorted_data:
     print(item)

#13). Python Dictionary program to add a key in a dictionary.

"""
Input= {1:’a’, 2:’b’}
Output= (1:’a’, 2:’b’, 3:’c’}
"""

print("_"*50)
dict1 = {1:'a', 2:'b'}
dict1.update({'c':3})
print(dict1)


#14). Python Dictionary program to concatenate two dictionaries.
"""
Input:
D1 = {‘name’ : ’yash’, ‘city’ :  ‘pune’}
D1 = {‘course’ : ’python’, ‘institute’ : ’sqatools’}
Output :
{ ‘name’ : ’yash’, city: ‘pune’, ‘course’ : ’python’, ‘institute’ : ’sqatools’ }
"""

print("_"*50)
d1={'name': 'yash', 'city': 'pune'}
d2={'course': 'python', 'institute': 'sqatools'}
d1.update(d2)
print(d1)

#15). Python Dictionary program to swap the values of the keys in the dictionary.

"""
Input = {name:’yash’, city: ‘pune’}
Output = {name:’pune’, city: ‘yash’}
"""
print("_"*50)
d1={'name': 'yash', 'city': 'pune'}
d2={}
for key, val in d1.items():
    d2[val]=key
print(d2)

#16). Python Dictionary program to get the sum of all the items in a dictionary.

"""
Input = {‘x’ : 23, ‘y’ : 10 , ‘z’ : 7}
Output = 40

"""
print("_"*50)
d1={'x':23, 'y':10, 'z':7}
total =0
for val in d1.values():
    total+=val
print(total)