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


# 11). Python Dictionary program to sort a dictionary using keys.
"""Input = {‘d’ : 21, ‘b’ : 53,  ‘a’: 13, ‘c’: 41}
Output =
(‘a’, 13)
(‘b’, 53)
(‘c’, 41)
(‘d’, 21)"""

d11 = {'d' : 21, 'b' : 53,  'a': 13, 'c': 41}
dict1 = {}
for key in sorted(d11):
    print((key, d11[key]))

# 12). Python Dictionary program to sort a dictionary in python using values.
#Input = {‘d’ : 14, ‘b’ : 52,  ‘a’: 13, ‘c’: 1 }
#Output= (c, 1) (a,13) (d, 14) (b, 52)

d12 = {'d' : 14, 'b' : 52,  'a': 13, 'c': 1 }
result= {key: value for key, value in sorted(d12.items(), key=lambda item:item[1])}
print(result)

sorted_d = dict(sorted(d12.items(), key=lambda x: x[1]))
print(sorted_d)

# 13). Python Dictionary program to add a key in a dictionary.
#Input= {1:’a’, 2:’b’}
#Output= (1:’a’, 2:’b’, 3:’c’}

d13 = {1:'a', 2:'b'}
d13.update({3:'c'})
print(d13)

# 14). Python Dictionary program to concatenate two dictionaries.
"""Input:
D1 = {‘name’ : ’yash’, ‘city’ :  ‘pune’}
D1 = {‘course’ : ’python’, ‘institute’ : ’sqatools’}
Output :
{ ‘name’ : ’yash’, city: ‘pune’, ‘course’ : ’python’, ‘institute’ : ’sqatools’ }"""

D1 = {'name' : 'yash', 'city' :  'pune'}
D2 = {'course' : 'python', 'institute' : 'sqatools'}

D1.update(D2)
print(D1)

# 15). Python Dictionary program to swap the values of the keys in the dictionary.
#Input = {name:’yash’, city: ‘pune’}
#Output = {name:’pune’, city: ‘yash’}

d15 = {'name':'yash', 'city': 'pune'}
data = list(d15.values())
result = {
    'name' : data[1],
    'city': data[0]
}
print(result)

k1,k2 = d15.keys()
v1,v2 = d15.values()
result = {k1:v2, k2:v1}
print(result)

# 16). Python Dictionary program to get the sum of all the items in a dictionary.
#Input = {‘x’ : 23, ‘y’ : 10 , ‘z’ : 7}
#Output = 40

d16 = {'x' : 23, 'y' : 10 , 'z' : 7}
total = 0
for val in d16.values():
    total += val
print(total)

# 17). Python program to get the size of a dictionary in python.
#Hint : use sys.getsizeof(var) method.
#Input = {‘name’ : ’virat’, ‘sport’ : ’cricket’}
#Output = 232bytes
import sys

d17 = {'name' : 'virat', 'sport' : 'cricket'}
print("size of: " + str(sys.getsizeof(d17)) + " bytes")

# 18). Python Dictionary program to check whether a key exists in the dictionary or not.
"""Input:
Dict1 = {city:’pune’, state=’maharashtra’}
Dict1[country]
Output= ‘key does not exist in dictionary"""

d18 = {'city':'pune', 'state':'maharashtra'}
count = 0
for key in d18.keys():
    if key == "country":
        count += 1
if count>0:
    print("key exist in dictionary")
else:
    print("key does not exist in dictionary")

# 19). Python program to iterate over a dictionary.
"""Input :
Dict1 = {food:’burger’, type:’fast food’}
Output :
food : burger
type : fast food"""

Dict1 = {'food':'burger', 'type':'fast food'}      
for v in Dict1:
    print(v, ":", Dict1[v])

# 20). Python Dictionary program to create a dictionary in the form of (n^3) i.e. if key=2 value=8
#Input: n=4
#Output ={1 : 1, 2 : 8, 3 : 27, 4 : 64}
dict1 = {}
for val in range(1,5):
    dict1[val] = val**3

print(dict1)

# 21). Python Dictionary program to insert a key at the beginning of the dictionary.
#Input = { ‘course’ : ’python’,  ‘institute’ : ’sqatools’ }
#Insert : ( ‘name’ : ’omkar’ )
#Output= { ‘name’ : ’omkar’, ‘course’ : ’python’, ‘institute’ : ’sqatools’}

Input = {'course' : 'python',  'institute' : 'sqatools' }
Insert = {'name' : 'omkar'}
Input.update(Insert)
print(Input)

# 22). Python Dictionary  program to create a dictionary where keys are between 1 to 5 and values are squares of the keys.
#Output ={1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25}
dict1 = {}
for val in range(1,6):
    dict1[val] = val**2
print(dict1)

# 23). Python Dictionary program to find the product of all items in the dictionary.
#Input = { ‘a’ : 2, ‘b’ : 4, ‘c’ : 5}
#Output = 40

d23 = { 'a' : 2, 'b' : 4, 'c' : 5}
output = 1
for val in d23.values():
    output = output*val
print(output)

# 24). Python Dictionary program to remove a key from the dictionary.
#Input = {a:2,b:4,c:5}
#Output = (a:1,b:4}

d24 = {'a':2, 'b':4, 'c':5}
d24.pop('c')
print(d24)

# 25). Python Dictionary program to map two lists into a dictionary.
"""Input : 
a = [ ‘name’, ‘sport’, ‘rank’, ‘age’]
b = [‘Virat’, ‘cricket’, 1,  32]
Output =  { ‘name’ : ’virat’, ‘sport’ : ’cricket’, ‘rank’: 1, ‘age’ : 32}"""

a = ['name', 'sport', 'rank', 'age']
b = ['Virat', 'cricket', 1,  32]

dict1 = {}
dict1 = dict(zip(a,b))
print(dict1)

# 26). Python Dictionary program to find maximum and minimum values in a dictionary.
"""Input :
Dict = { ‘a’ : 10, ‘b’ : 44 , ‘c’ : 60, ‘d’ : 25}
Output :
Maximum value: 60
Minimum value: 10 """

dict1 = { 'a' : 10, 'b' : 44 , 'c' : 60, 'd' : 25}
list1 = []
for val in dict1.values():
    list1.append(val)
print("Maximum value:", max(list1))
print("Minimum value:", min(list1))

# 27). Python Dictionary program to group the same items into a dictionary value.
##Input :
#list = [1,3,4,4,2,5,3,1,5,5,2,]
#Output = {1 : [1, 1], 2 :[2, 2], 3 : [3, 3], 4 : [4, 4], 5 : [5, 5, 5]}
from collections import defaultdict
list1 = [1,3,4,4,2,5,3,1,5,5,2]
dict1 = defaultdict(list)
for val in list1:
    dict1[val].append(val)
print(dict1)
    
# 28). Python Dictionary program to replace words in a string using a dictionary.
#String = ’learning python at sqa-tools’
#Dict = { ‘at’ : ’is’, ‘sqa-tools’ : ’fun’}
#Output = ‘learning python is fun’

string = 'learning python at sqa-tools'
dict1 = { 'at' : 'is', 'sqa-tools' : 'fun'}
for key, value in dict1.items():
    string = string.replace(key , value)
print(string)

# 29). Python Dictionary program to remove a word from the string if it is a key in a dictionary.
#String = ’sqatools is best for learning python’
#Dict = { ‘best’ : 2, ‘learning’ : 6}
#Output = “sqatools is for python”

string = 'sqatools is best for learning python'
list1 = string.split(" ")
str2 = ''
dict1 = { 'best' : 2, 'learning' : 6}
print(list1)
for word in list1:
    if word not in dict1:
        str2 = str2 + word + " "
print(str2)

# 30). Python Dictionary program to remove duplicate values from dictionary values.
#Input:
#Dict1 = { ‘marks1’ : [23,28,23,69], ‘marks2’ : [ 25, 14,25] }
#Output= { ‘marks1’ : [28, 69], ‘marks2’ : [14,19] }

d30 = { 'marks1' : [23,28,23,69], 'marks2' : [ 25, 14,25] }

for key, val in d30.items():
    for ele in val:
        if ele in val:
            val.remove(ele)
print(d30)

# 31). Python Dictionary program to check whether a dictionary is empty or not.
#Input:
#Dict1 = {}
#Output: Given dictionary is empty

dict1 = {}
if len(dict1)>0:
    print("Given dictionary is not empty")
else:
    print("Given dictionary is empty")


# 32). Python Dictionary program to add two dictionaries if the keys are the same then add their value.
#Input:
#Dict1 = { ‘x’:10, ‘y’:20, ‘c’:50, ‘f’:44 }
#Dict2 = {‘x’:60,’c’:25,’y’:56}
#Output = {‘x’: 70, ‘c’: 75, ‘y’: 76}
dict1 = { 'x':10, 'y':20, 'c':50, 'f':44 }
dict2 = { 'x':60, 'c':25, 'y':56}
for key in dict1:
    for k in dict2:
        if key == k:
            a = dict1[key]+dict2[key]
            dict2[key] =a
print(dict2)

# 33). Python Dictionary program to print all the unique values in a dictionary.
#Input :
#Dict1 = [{name1:’robert’},  {name2:’john’}, {name3:’jim’}, {name4:’robert’}]
#Output = [‘robert’, ’john’, ’jim’]

d33 = [{'name1':'robert'},  {'name2':'john'}, {'name3':'jim'}, {'name4':'robert'}]
output = []
for value in d33:
    for key, val in value.items():
        if val not in output:
            output.append(val)
print(output)

# 34). Python Dictionary program to display different combinations of letters from dictionary values.
"""Input:
Dict1 = { x:[e,f], y:[a,b]}
Output: 
  ea
  eb
  fa
  fb"""

import itertools
d = { 'x':['e','f'], 'y':['a','b']}
for a in itertools.product(*d.values()):
    print(''.join(a))

# 35). Python Dictionary program to create a dictionary from a string.
#Input = ‘sqatools’
#Output = {s:2,q:1,a:1, t:1,o:2, l:1}
d35 = "sqatools"
dict1 = {}
for ch in d35:
    dict1[ch] = d35.count(ch)
print(dict1)

# 36). Python Dictionary program to print the given dictionary in the form of tables.
"""Input:
Dict1= {names:[‘virat’,’messi’,’kobe’], sport:[‘cricket’,’football’,’basketball’]}
Output:
     Names   sport
0    Virat      cricket
1    Messi     football
2    Kobe      basketball"""

import pandas as pd
dict1 = {'names':['virat','messi','kobe'], 'sport':['cricket','football','basketball']}
table = pd.DataFrame(dict1)
print(table)

# 37). Python program to count frequencies in a list using a dictionary.
"""Input:
list1= [2,5,8,1,2,6,8,5]
Output = {1:1,2:2, 5:2, 6:1, 8:2}"""
list37 = [2,5,8,1,2,6,8,5]
dict1 = {}
for val in sorted(list37):
    dict1[val] = list37.count(val)
print(dict1)


from collections import defaultdict
list37 = [2,5,8,1,2,6,8,5]
dict1 = defaultdict(list)
for val in sorted(list37):
    dict1[val].append(val)
print(dict1)

# 38). Python program to find mean of values of keys in a dictionary.
"""Input :
Dict1= {m1:25, m2:20, m3:15}
Output :
Mean is 20"""

dict38 = {'m1':25, 'm2':20, 'm3':15}
total = 0
count = 0
for val in dict38.values():
    total += val
    count += 1
print("Mean:", total//count )

# 39). Python program to convert a list into a nested dictionary of keys.
#Input = ['a','b','c','d']
#Output = {'a: {'b'': {'c': {'d': {}}}}}

d39 = ['a','b','c','d']
new_dict = current = {}
for char in d39:
    current[char] = {}
    current = current[char]
print(new_dict)

# 40). Python program to sort a list of values in a dictionary.
#Input= { a1 : [1,5,3], a2 : [10,6,20] }
#Output= ( a1 : [1,3,5], a2 : [6,10,20] }

d40 = {'a1' : [1,5,3], 'a2' : [10,6,20]}
dict1 = {}
for key, val in d40.items():
    val.sort()
    dict1[key] = val
print(dict1)

# 41). Python program to get a product with the highest price from a dictionary.
#Input = { ‘price1’ : 450, ‘price2‘ : 600,  ‘price3′ : 255,  ‘price4′ : 400}
#Output = P2 500

d41 = { 'price1' : 450, 'price2' : 600,  'price3' : 255,  'price4' : 400}
price = 0
name = 0
for key, val in d41.items():
    if val>price:
        price = val
        name = key
print("Product name:", name)
print("Product price:", price)

# 42). Python program to print a dictionary line by line.
"""Input = {‘virat’: {sport:’cricket’, team:’india’}, ‘messi’: {sport:’football’, team:’argentina’}}
Output=
Virat
Sport : cricket
Team : india

Messi
Sport : football
Team : argentina"""

d42 = {'virat': {'sport':'cricket', 'team':'india'}, 'messi': {'sport':'football', 'team':'argentina'}}
for key, val in d42.items():
    print(key)
    for k,v in val.items():
        print(k, ":", v)

# 43). Python program to convert a key value list dictionary into a list of list.
#Input = {sqa:[1,4,6], tools:[3,6,9]}
#Output= [[sqa,1,4,6],[tools,3,6,9]]

d43 = {'sqa':[1,4,6], 'tools':[3,6,9]}
list1 = []
for key, val in d43.items():
    temp = [key]+val
    list1.append(temp)
print(list1)

# 44). Python program to convert a list of dictionaries to a list of lists.
#Input= [{‘sqa’:123,’tools’:456}]
#Output= [[sqa],[tools],[123],[456]]
d44 = [{'sqa':123,'tools':456}]
output = []
for data in d44:
    for k,v in data.items():
        output.append([k])
        output.append([v])
print(output)

# 45). Python program to count a number of items in a dictionary value that is in a list.
#Input = {‘virat’:[‘match1’,match2’,’match3’], ‘rohit’:[‘match1’,’match2’]}
#Output= 5

d45 = {'virat':['match1','match2','match3'], 'rohit':['match1','match2']}
total = 0
for val in d45.values():
    if type(val) == list:
        for data in val:
            total += 1
print(total)

# 46). Python program to sort items in a dictionary in descending order.
#Input = {‘Math’:70, ‘Physics’:90, ‘Chemistry’:67}
#Output = {‘Physics’:90, ’Maths’:70, ’Chemistry’:67}

d46 = {'Math':70, 'Physics':90, 'Chemistry':67}
output = dict(sorted(d46.items(), key = lambda val : val[1], reverse=True))
print(output)

# 47). Python program to replace dictionary values with their average.
#Input = { name:’ketan’, subject:’maths’, p1:80, p2:70}
#Output = { name:’ketan’,subject:’maths’, p1+p2:75}

d47 = {'name':'ketan', 'subject':'maths', 'p1':80, 'p2':70}
n1 = d47.pop('p1')
n2 = d47.pop('p2')
d47['p1+p2'] = (n1+n2)/2
print(d47)

# 48). Python program to match key values in two dictionaries.
#Input: 
#A = {‘k1’: p, ‘k2’: q, ‘k3’: r}
#B = {‘k1’: p, ‘k2’: s}

#Output = k1: p is present in both A and B

a = {'k1': 'p', 'k2': 'q', 'k3': 'r'}
b = {'k1': 'p', 'k2': 's'}
for key in a:
    if key in b and a[key] == b[key]:
        print(f"{key}: {a[key]} is present in both a and b")

# 49). Python program to create a dictionary of keys a, b, and c where each key has as value a list from 1-5, 6-10, and 11-15 respectively. 
#Output = { a: [1,2,3,4,5],  b: [6,7,8,9,10],  c: [11,12,13,14,15] }
l1 = []
l2 = []
l3 = []
for i in range(1,6):
    l1.append(i)
for i in range(6,11):
    l2.append(i)
for i in range(11,16):
    l3.append(i)
dict1 = {}
dict1['a'] = l1
dict1['b'] = l2
dict1['c'] = l3
print(dict1)

# 50). Python program to drop empty Items from a given dictionary.
#Input = {‘m1’:40, ‘m2’:50, ‘m3’:None}
#Output = {‘m1’:40, ‘m2’:50}

d50 = {'m1':40, 'm2':50, 'm3':None}
dict1 = {}
for key,val in d50.items():
    if val != None:
        dict1[key] = val
print(dict1)

# 51). Python program to filter a dictionary based on values.
#Input= { ‘alex’ : 50,  ‘john’ : 45, ‘Robert’ : 30}
#Output= value greater than 40
#{alex:50, john:45}

d51 = {'alex' : 50,  'john' : 45, 'Robert' : 30}
dict1 = {}
for key, val in d51.items():
    if val > 40:
        dict1[key] = val
print(dict1)

# 52). Python program to convert a key-values list to a flat dictionary.
#Input = {‘name’: [‘Apr’, ‘May’, ‘June’], ‘month’: [4, 5, 6]}
#Output ={‘Apr’: 4, ‘May’: 5, ‘June’: 6}

d52 = {'name': ['Apr', 'May', 'June'], 'month': [4, 5, 6]}
dict1 = dict(zip(d52['name'], d52['month']))
print(dict1)

# 53). Python program to convert a list of Tuples into a dictionary
#Input =  [(“mike”, 1), (“Sarah”, 20), (“Jim”, 16)]
#Output = {“mike”:1, “Sarah”:20, “Jim”:16}

d53 = [('mike', 1), ('Sarah', 20), ('Jim', 16)]